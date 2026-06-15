"""
Scenario definitions and runners.
"""

import numpy as np
from .model import (
    Params, solve_qre, welfare_metrics,
    find_resort_nash, find_social_optimum, check_multiplicity,
)


# Fixed pricing scenarios (exogenous, for comparison)
_FIXED = {
    'no_specialization': {
        'label': 'No Specialization\n(uniform)',
        'prices': np.full(5, 0.5),
    },
    'mild_specialization': {
        'label': 'Mild Specialization\n(2 premium + 3 budget)',
        'prices': np.array([0.9, 0.9, 0.5, 0.3, 0.3]),
    },
    'strong_specialization': {
        'label': 'Strong Specialization\n(tiered)',
        'prices': np.array([2.0, 1.2, 0.6, 0.3, 0.1]),
    },
}


def _run_one(name, prices, params, label=None):
    x_H, x_L = solve_qre(prices, params)
    m = welfare_metrics(prices, x_H, x_L, params)
    return {
        'name': name,
        'label': label or name,
        'prices': prices.copy(),
        'x_H': x_H,
        'x_L': x_L,
        **m,
    }


def run_all_scenarios(params=None, verbose=True):
    """
    Run all five scenarios and return a dict of results.

    Scenarios
    ---------
    no_specialization    : all resorts at price 0.5
    mild_specialization  : 2 premium (0.9) + 3 budget (0.3/0.5)
    strong_specialization: fully tiered (2.0 down to 0.1)
    resort_nash          : each resort maximizes own revenue (Nash equilibrium)
    social_optimum       : prices that maximize intrinsic value (total surplus)
    """
    if params is None:
        params = Params()

    results = {}

    for name, cfg in _FIXED.items():
        if verbose:
            print(f"  {name} ...")
        results[name] = _run_one(name, cfg['prices'].copy(), params, cfg['label'])

    if verbose:
        print("  resort_nash (iterated best-response) ...")
    p_nash = find_resort_nash(params)
    results['resort_nash'] = _run_one(
        'resort_nash', p_nash, params, 'Resort Nash\n(revenue-maximizing)'
    )

    if verbose:
        print("  social_optimum (Nelder-Mead) ...")
    p_opt = find_social_optimum(params)
    results['social_optimum'] = _run_one(
        'social_optimum', p_opt, params, 'Social Optimum\n(intrinsic value)'
    )

    return results


def price_spread_analysis(params=None, n_points=30):
    """
    Sweep price spread from 0 (uniform) to 2.0 (strongly tiered).
    Prices are linearly spaced from p_low to p_high, centered at 0.5.
    Returns a list of dicts with 'spread' plus all welfare metrics.
    """
    if params is None:
        params = Params()

    spreads = np.linspace(0.0, 2.0, n_points)
    results = []
    for spread in spreads:
        p_low = max(0.05, 0.5 - spread / 2)
        p_high = 0.5 + spread / 2
        prices = np.linspace(p_low, p_high, params.n_resorts)
        x_H, x_L = solve_qre(prices, params)
        m = welfare_metrics(prices, x_H, x_L, params)
        results.append({'spread': float(spread), 'prices': prices, **m})

    return results


def multiplicity_demo(params=None):
    """
    Demonstrate the wrong-equilibrium trap: same prices, different equilibria.
    Uses higher rationality (lam=15) to expose multiple fixed points.
    """
    if params is None:
        params = Params()

    high_lam = Params(
        N_H=params.N_H, N_L=params.N_L, n_resorts=params.n_resorts,
        alpha_H=params.alpha_H, alpha_L=params.alpha_L,
        beta_H=params.beta_H, beta_L=params.beta_L,
        gamma_H=params.gamma_H, gamma_L=params.gamma_L,
        lam=15.0, damping=0.2, n_iter=5000,
    )

    prices_uniform = np.full(params.n_resorts, 0.5)
    equilibria = check_multiplicity(prices_uniform, high_lam, n_starts=40)
    return equilibria, high_lam
