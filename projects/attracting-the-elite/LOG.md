# Log: Attracting the Elite

---

## 2026-06-15 -- Simulator built

**What happened:** Built a Python simulator in `sim/` and a top-level `run_sim.py` entry point. Run with `python run_sim.py` from the project directory.

**Model:** 5 ski resorts, 1000 tourists (80% moderate L, 20% rich H). Resort $j$ sets price $p_j$. Tourist payoff:
$$u_i(j) = -\alpha_i p_j + \beta_i \text{frac}_H(j) - \gamma_i \text{cong}(j)$$
with $\alpha_H < \alpha_L$ (H less price-sensitive), $\beta_H > \beta_L$ (H value composition more), $\gamma_H > \gamma_L$ (H dislike congestion more). Equilibrium is a Quantal Response Equilibrium (logit fixed point, $\lambda=8$). Social welfare = intrinsic value (price is a pure transfer, so consumer + producer surplus cancels price out).

**Key findings from 5 scenarios:**

| Scenario | Intrinsic (social) | Tourist welfare | Revenue | Segregation |
|---|---|---|---|---|
| No specialization (uniform p=0.5) | 0.040 | -0.480 | 500 | 0.000 |
| Mild specialization (0.9/0.9/0.5/0.3/0.3) | **0.088** | -0.358 | 492 | 0.311 |
| Strong specialization (2.0/1.2/0.6/0.3/0.1) | 0.070 | -0.211 | 417 | 0.393 |
| Resort Nash (revenue-maximizing) | 0.071 | -0.829 | **1012** | 0.396 |
| Social optimum (intrinsic-maximizing) | **0.134** | **-0.028** | 324 | 0.399 |

**Interpretation:**
- Mild price specialization substantially beats no specialization in social surplus (0.088 vs 0.040) -- sorting gains dominate the transfer effect.
- *Too much* specialization hurts: strong specialization (spread=1.9) falls below mild (spread=0.6). The spread analysis finds a peak in intrinsic value at spread ~0.5, after which cheap resorts become overcrowded.
- Resort Nash extracts maximal revenue but destroys tourist welfare (heavy price markup; surplus extraction with no efficiency gain).
- Social optimum uses low prices on most resorts with a few selective high prices -- a binary instrument that concentrates H at 2 resorts (frac_H near 1) while keeping costs low for L tourists. This is a mechanism design result: prices serve as allocation tools, not as a revenue instrument.
- At high price spreads, rich tourists reach *positive* welfare (exclusive, uncrowded resorts at still-affordable prices) while moderate tourists fall into negative welfare (overcrowded cheap resorts). This is the composition externality at work.

**Files:**
- `sim/model.py` -- payoff function, QRE solver, resort Nash, social optimum
- `sim/scenarios.py` -- scenario runner, price spread sweep, multiplicity check
- `sim/plots.py` -- all figures
- `run_sim.py` -- entry point
- `sim/figures/` -- distributions, welfare comparison, composition, spread analysis, multiplicity

**Next step:** Use the spread analysis as a phase diagram backbone -- map the price spread vs. N_H/N population share to find where specialization is beneficial. Sketch the formal model.

---

## 2026-06-15 -- Literature mapping and research question refinement

**What happened:** Mapped the existing literature to locate the precise gap. Key finding: congestion games (Rosenthal 1973, Sandholm 2010) reduce the externality to scalar load or aggregate mass; club-good models (Buchanan 1965, Scotchmer 1994) capture composition preferences but are static and non-strategic on the destination side; Schelling (1971) has composition thresholds but no strategic destinations. None combine composition-dependent payoffs $u_i(n^H_\ell, n^L_\ell)$ with asymmetric cross-type derivatives and a strategic destination layer.

**Key decisions:**
- The novel theoretical core is a two-destination, two-type congestion game with composition-dependent payoffs and strategic destination pricing -- proving when a separating equilibrium exists and what breaks it.
- Closest anchors to build from: Milchtaich (1996) for player-specific congestion, Sandholm (2010) for the population game framework, Scotchmer (2002) for composition-in-clubs.
- Butler's TALC lifecycle is the empirical phenomenon to formalize; Venice, Santorini, Bhutan are natural empirical targets.

**Refined research question:** How to design price and amenity instruments for a destination competing for two tourist types under composition-dependent payoffs $u_i(n^H_\ell, n^L_\ell)$, such that a separating equilibrium exists and is stable against low-type invasion?

**Next step:** Run targeted literature search to catch recent work on composition-dependent congestion games; sketch the formal model (equilibrium characterization + screening problem).

---

## 2026-06-15 -- Project kickoff and brainstorming

**What happened:** Initial brainstorming session on population games and tourism. Identified the core setup: heterogeneous tourist types with different congestion sensitivities, destinations as strategic agents choosing instruments in a Stackelberg game over the tourist population equilibrium.

**Key decisions:**
- Frame as a population game (not a static game) to capture dynamics of how tourist type-distributions shift over time.
- Composition-dependent payoffs (not just count-dependent) are the distinguishing structural feature.
- The "wrong equilibrium trap" is the central phenomenon to explain and solve.

**Next step:** Targeted literature search to confirm gaps in (1) heterogeneous-type congestion games and (2) mechanism design over population game equilibria in tourism contexts.
