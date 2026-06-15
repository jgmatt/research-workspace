"""
Ski resort competition model with heterogeneous tourists.

Five resorts compete for tourists via price p_j.
Two tourist types:
  H (rich):     20% of population -- less price-sensitive, more composition/congestion-averse
  L (moderate): 80% of population -- more price-sensitive, less composition/congestion-averse

Payoff for type i at resort j:
    u_i(j) = -alpha_i * p_j + beta_i * frac_H(j) - gamma_i * cong(j)
where
    frac_H(j) = n_H_j / n_j          (fraction of rich at resort j)
    cong(j)   = n_j / N              (normalized load)

Equilibrium: Quantal Response Equilibrium (logit fixed point, rationality param lam).
Total surplus = intrinsic value (since price is a pure transfer between tourist and resort).
"""

import numpy as np
from dataclasses import dataclass
from scipy.optimize import minimize_scalar, minimize


@dataclass
class Params:
    # Population
    N_H: int = 200       # rich tourists
    N_L: int = 800       # moderate tourists
    n_resorts: int = 5

    # Price sensitivity  (H less sensitive)
    alpha_H: float = 0.4
    alpha_L: float = 1.2

    # Composition preference (both like high frac_H; H more so)
    beta_H: float = 1.2
    beta_L: float = 0.6

    # Congestion aversion (both dislike crowds; H more so)
    gamma_H: float = 1.0
    gamma_L: float = 0.4

    # QRE rationality: higher -> sharper best-response
    lam: float = 8.0

    # Fixed-point solver
    n_iter: int = 2000
    tol: float = 1e-10
    damping: float = 0.5   # fraction of new iterate used each step

    @property
    def N(self):
        return self.N_H + self.N_L


def _softmax(v):
    e = np.exp(v - v.max())
    return e / e.sum()


def payoffs(prices, x_H, x_L, p):
    """
    Return (u_H, u_L): payoff vectors over resorts for each type.
    x_H, x_L: fraction of each type at each resort (sums to 1).
    """
    n_H = x_H * p.N_H
    n_L = x_L * p.N_L
    n_j = n_H + n_L
    frac_H = np.where(n_j > 1e-9, n_H / n_j, p.N_H / p.N)
    cong = n_j / p.N
    u_H = -p.alpha_H * prices + p.beta_H * frac_H - p.gamma_H * cong
    u_L = -p.alpha_L * prices + p.beta_L * frac_H - p.gamma_L * cong
    return u_H, u_L


def solve_qre(prices, params, x0_H=None, x0_L=None):
    """
    Find the Quantal Response Equilibrium via damped logit iteration.
    Returns (x_H, x_L): fraction vectors at fixed point.
    """
    n = params.n_resorts
    x_H = x0_H.copy() if x0_H is not None else np.ones(n) / n
    x_L = x0_L.copy() if x0_L is not None else np.ones(n) / n
    d = params.damping

    for _ in range(params.n_iter):
        u_H, u_L = payoffs(prices, x_H, x_L, params)
        new_H = d * _softmax(params.lam * u_H) + (1 - d) * x_H
        new_L = d * _softmax(params.lam * u_L) + (1 - d) * x_L
        err = max(np.abs(new_H - x_H).max(), np.abs(new_L - x_L).max())
        x_H, x_L = new_H, new_L
        if err < params.tol:
            break

    return x_H, x_L


def welfare_metrics(prices, x_H, x_L, params):
    """
    Compute welfare metrics for a given equilibrium.

    tourist_welfare:  avg per-tourist payoff (includes price as cost)
    intrinsic:        avg per-tourist payoff WITHOUT price = social surplus
                      (price is a transfer, so consumer + producer surplus = intrinsic)
    revenue:          total resort revenue
    segregation:      weighted std of frac_H across resorts (0 = fully mixed)
    """
    u_H, u_L = payoffs(prices, x_H, x_L, params)
    n_j = x_H * params.N_H + x_L * params.N_L
    frac_H = np.where(n_j > 1e-9, x_H * params.N_H / n_j, params.N_H / params.N)

    tw_H = float(np.dot(u_H, x_H))
    tw_L = float(np.dot(u_L, x_L))
    tourist_welfare = (tw_H * params.N_H + tw_L * params.N_L) / params.N

    revenue = float(np.dot(prices, n_j))

    # Intrinsic value: u_i + alpha_i * p_j removes the price term
    iv_H = u_H + params.alpha_H * prices
    iv_L = u_L + params.alpha_L * prices
    intrinsic = float(
        (np.dot(iv_H, x_H) * params.N_H + np.dot(iv_L, x_L) * params.N_L) / params.N
    )

    w = n_j / n_j.sum()
    mu_frac = float(np.dot(frac_H, w))
    segregation = float(np.sqrt(np.dot(w, (frac_H - mu_frac) ** 2)))

    return {
        'tourist_welfare_H': tw_H,
        'tourist_welfare_L': tw_L,
        'tourist_welfare': tourist_welfare,
        'revenue': revenue,
        'intrinsic': intrinsic,
        'segregation': segregation,
        'frac_H': frac_H,
        'n_j': n_j,
    }


def find_resort_nash(params, p_init=None, p_range=(0.05, 3.0), n_outer=30):
    """
    Iterated best-response dynamics for resort pricing Nash equilibrium.
    Each resort maximizes own revenue p_j * n_j holding other prices fixed.
    """
    prices = p_init.copy() if p_init is not None else np.full(params.n_resorts, 0.5)

    for _ in range(n_outer):
        prev = prices.copy()
        for j in range(params.n_resorts):
            def neg_rev(p_j, _j=j):
                p = prices.copy()
                p[_j] = p_j
                x_H, x_L = solve_qre(p, params)
                n = x_H * params.N_H + x_L * params.N_L
                return -p_j * n[_j]

            res = minimize_scalar(neg_rev, bounds=p_range, method='bounded',
                                  options={'xatol': 5e-4})
            prices[j] = res.x

        if np.max(np.abs(prices - prev)) < 1e-3:
            break

    return prices


def find_social_optimum(params, p_range=(0.05, 3.0)):
    """
    Maximize intrinsic value (= total surplus) over resort prices.
    Tries multiple starting points and returns the best.
    """
    def neg_iv(prices):
        prices = np.clip(prices, *p_range)
        x_H, x_L = solve_qre(prices, params)
        m = welfare_metrics(prices, x_H, x_L, params)
        return -m['intrinsic']

    starts = [
        np.full(params.n_resorts, 0.4),
        np.full(params.n_resorts, 1.0),
        np.linspace(0.2, 2.0, params.n_resorts),
        np.linspace(2.0, 0.2, params.n_resorts),
        np.array([1.5, 1.0, 0.5, 0.3, 0.1]),
        np.array([0.1, 0.3, 0.5, 1.0, 1.5]),
    ]
    best_val, best_p = np.inf, starts[0].copy()
    for p0 in starts:
        res = minimize(neg_iv, p0, method='Nelder-Mead',
                       options={'maxiter': 5000, 'xatol': 5e-4, 'fatol': 1e-5})
        if res.fun < best_val:
            best_val = res.fun
            best_p = res.x.copy()

    return np.clip(best_p, *p_range)


def check_multiplicity(prices, params, n_starts=30, rng_seed=0):
    """
    Try many random initializations and return distinct equilibria found.
    Useful for detecting the wrong-equilibrium trap (multiple QRE for high lam).
    """
    rng = np.random.default_rng(rng_seed)
    found = []

    for _ in range(n_starts):
        x0_H = rng.dirichlet(np.ones(params.n_resorts))
        x0_L = rng.dirichlet(np.ones(params.n_resorts))
        x_H, x_L = solve_qre(prices, params, x0_H, x0_L)
        m = welfare_metrics(prices, x_H, x_L, params)
        frac = m['frac_H']

        is_new = all(
            np.max(np.abs(frac - prev['frac_H'])) > 0.04 for prev in found
        )
        if is_new:
            found.append({'x_H': x_H, 'x_L': x_L, **m})

    return found
