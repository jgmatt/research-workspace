"""
Run the ski resort simulator. Execute from this directory:

    python run_sim.py

Produces a summary table and four figures in sim/figures/.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from sim.model import Params
from sim.scenarios import run_all_scenarios, price_spread_analysis, multiplicity_demo
import sim.plots as viz

FIG_DIR = Path(__file__).parent / 'sim' / 'figures'
FIG_DIR.mkdir(parents=True, exist_ok=True)


def print_summary(results, params):
    SEP = '=' * 74
    print(f'\n{SEP}')
    print(f'{"Scenario":<32} {"Intrinsic":>9} {"T.Welfare":>10} {"Revenue":>9} {"Seg.":>6}')
    print('-' * 74)
    for name, r in results.items():
        label = r['label'].replace('\n', ' ')
        p_str = '[' + ' '.join(f'{p:.2f}' for p in r['prices']) + ']'
        print(f'{label:<32} {r["intrinsic"]:>9.4f} {r["tourist_welfare"]:>10.4f} '
              f'{r["revenue"]:>9.1f} {r["segregation"]:>6.4f}')
        print(f'  prices: {p_str}')
    print(SEP)

    # Which scenario has best intrinsic value and why
    best_iv = max(results.values(), key=lambda r: r['intrinsic'])
    best_tw = max(results.values(), key=lambda r: r['tourist_welfare'])
    print(f'\nHighest intrinsic value (social surplus): {best_iv["label"].replace(chr(10)," ")}')
    print(f'Highest tourist welfare:                  {best_tw["label"].replace(chr(10)," ")}')
    print()


def main():
    params = Params()

    print(f'Population: {params.N_H} rich (H) + {params.N_L} moderate (L) = {params.N} tourists')
    print(f'Resorts: {params.n_resorts} | QRE rationality lambda = {params.lam}')
    print(f'Payoff params: alpha_H={params.alpha_H}, alpha_L={params.alpha_L}, '
          f'beta_H={params.beta_H}, beta_L={params.beta_L}, '
          f'gamma_H={params.gamma_H}, gamma_L={params.gamma_L}')
    print()

    print('Running scenarios...')
    results = run_all_scenarios(params, verbose=True)
    print_summary(results, params)

    print('Running price spread analysis (30 points)...')
    spread = price_spread_analysis(params, n_points=30)
    print('  Done.')

    print('Checking for multiple equilibria (uniform prices, high rationality)...')
    equilibria, trap_params = multiplicity_demo(params)
    n_eq = len(equilibria)
    print(f'  Found {n_eq} distinct equilibri{"um" if n_eq == 1 else "a"}.')

    print('\nSaving figures...')
    viz.plot_distributions(results, params,
                           save_to=FIG_DIR / 'distributions.png')
    print('  distributions.png')

    viz.plot_welfare_comparison(results,
                                save_to=FIG_DIR / 'welfare_comparison.png')
    print('  welfare_comparison.png')

    viz.plot_composition(results, params,
                         save_to=FIG_DIR / 'composition.png')
    print('  composition.png')

    viz.plot_spread_analysis(spread,
                             save_to=FIG_DIR / 'spread_analysis.png')
    print('  spread_analysis.png')

    if equilibria:
        viz.plot_multiplicity(equilibria, params,
                              save_to=FIG_DIR / 'multiplicity.png')
        print('  multiplicity.png')

    print(f'\nAll figures saved to {FIG_DIR}/')


if __name__ == '__main__':
    main()
