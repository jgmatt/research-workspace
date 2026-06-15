"""
Visualization for the ski resort simulator.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 9,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
})

RESORT_LABELS = ['R1', 'R2', 'R3', 'R4', 'R5']
C_H = '#E8A317'   # gold -- rich tourists
C_L = '#4A7FBF'   # steel blue -- moderate tourists

SCENARIO_ORDER = [
    'no_specialization',
    'mild_specialization',
    'strong_specialization',
    'resort_nash',
    'social_optimum',
]


def _abbrev(label):
    return label.replace('\n', ' ')


def plot_distributions(results, params, save_to=None):
    """
    Stacked bar chart of tourist distribution for each scenario.
    One column per scenario.
    """
    order = [k for k in SCENARIO_ORDER if k in results]
    n_scen = len(order)

    fig, axes = plt.subplots(1, n_scen, figsize=(3.2 * n_scen, 4.2), sharey=True)
    if n_scen == 1:
        axes = [axes]

    for ax, key in zip(axes, order):
        r = results[key]
        x = np.arange(params.n_resorts)
        n_H = r['x_H'] * params.N_H
        n_L = r['x_L'] * params.N_L

        ax.bar(x, n_L, color=C_L, label='Moderate (L)', zorder=2)
        ax.bar(x, n_H, bottom=n_L, color=C_H, label='Rich (H)', zorder=2)

        # Price annotation above each bar
        for i, (p, nH, nL) in enumerate(zip(r['prices'], n_H, n_L)):
            ax.text(i, nH + nL + 8, f'p={p:.2f}',
                    ha='center', va='bottom', fontsize=7, color='#333333')

        ax.axhline(params.N / params.n_resorts, color='gray',
                   linestyle=':', linewidth=1.0, zorder=1)
        ax.set_xticks(x)
        ax.set_xticklabels(RESORT_LABELS)
        ax.set_title(_abbrev(r.get('label', key)), fontsize=8.5, pad=3)
        ax.set_ylim(0, params.N * 0.75)

    axes[0].set_ylabel('Number of tourists')
    patch_L = mpatches.Patch(color=C_L, label='Moderate (L)')
    patch_H = mpatches.Patch(color=C_H, label='Rich (H)')
    fig.legend(handles=[patch_L, patch_H], loc='upper center',
               ncol=2, fontsize=8, bbox_to_anchor=(0.5, 1.01))
    fig.suptitle('Tourist distribution by resort and scenario',
                 fontsize=10, y=1.06)
    fig.tight_layout()

    if save_to:
        fig.savefig(save_to, dpi=150, bbox_inches='tight')
    return fig


def plot_welfare_comparison(results, save_to=None):
    """
    Side-by-side bar charts for intrinsic value, tourist welfare, and segregation.
    """
    order = [k for k in SCENARIO_ORDER if k in results]
    labels = [_abbrev(results[k].get('label', k)) for k in order]
    x = np.arange(len(order))

    panels = [
        ('intrinsic',        'Intrinsic Value\n(= Social Surplus)', '#6ABF69'),
        ('tourist_welfare',  'Tourist Welfare\n(incl. price paid)',  '#4A7FBF'),
        ('segregation',      'Segregation Index\n(std of frac_H)',   '#E87A5D'),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    for ax, (key, title, color) in zip(axes, panels):
        vals = [results[k][key] for k in order]
        bars = ax.bar(x, vals, color=color, edgecolor='white', linewidth=0.5, zorder=2)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=7.5, rotation=20, ha='right')
        ax.set_title(title, fontsize=9)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + abs(bar.get_height()) * 0.02,
                    f'{v:.3f}', ha='center', va='bottom', fontsize=7)

    fig.suptitle('Welfare metrics by scenario', fontsize=11)
    fig.tight_layout()

    if save_to:
        fig.savefig(save_to, dpi=150, bbox_inches='tight')
    return fig


def plot_composition(results, params, save_to=None):
    """
    Line plot of frac_H at each resort, one line per scenario.
    """
    order = [k for k in SCENARIO_ORDER if k in results]
    x = np.arange(params.n_resorts)
    markers = ['o', 's', '^', 'D', 'v']
    linestyles = ['-', '--', '-.', ':', (0, (3, 1, 1, 1))]

    fig, ax = plt.subplots(figsize=(8, 4))
    for key, marker, ls in zip(order, markers, linestyles):
        r = results[key]
        label = _abbrev(r.get('label', key))
        ax.plot(x, r['frac_H'], marker=marker, linestyle=ls,
                linewidth=1.8, label=label, zorder=2)

    ax.axhline(params.N_H / params.N, color='black', linestyle=':',
               linewidth=1.0, label=f'Overall H fraction ({params.N_H/params.N:.0%})')
    ax.set_xticks(x)
    ax.set_xticklabels(RESORT_LABELS)
    ax.set_ylabel('Fraction of rich tourists (frac_H)')
    ax.set_ylim(0, 1)
    ax.set_title('Rich-tourist composition by resort and scenario')
    ax.legend(fontsize=8, loc='upper right')
    fig.tight_layout()

    if save_to:
        fig.savefig(save_to, dpi=150, bbox_inches='tight')
    return fig


def plot_spread_analysis(spread_results, save_to=None):
    """
    Show how intrinsic value, tourist welfare (H and L), and segregation
    evolve as the price spread increases.
    """
    spreads = [r['spread'] for r in spread_results]

    fig, axes = plt.subplots(1, 3, figsize=(13, 4))

    panels = [
        ('intrinsic',           'Intrinsic Value (Social Surplus)', '#6ABF69'),
        ('tourist_welfare',     'Avg Tourist Welfare (incl. price)',  '#4A7FBF'),
        ('segregation',         'Segregation Index',                  '#E87A5D'),
    ]

    for ax, (key, title, color) in zip(axes, panels):
        ax.plot(spreads, [r[key] for r in spread_results], color=color, linewidth=2)
        ax.set_xlabel('Price spread (max price - min price)')
        ax.set_title(title, fontsize=9)

    # Overlay H and L welfare on the tourist welfare panel
    axes[1].plot(spreads, [r['tourist_welfare_H'] for r in spread_results],
                 color=C_H, linewidth=1.2, linestyle='--', label='Rich (H)')
    axes[1].plot(spreads, [r['tourist_welfare_L'] for r in spread_results],
                 color=C_L, linewidth=1.2, linestyle='--', label='Moderate (L)')
    axes[1].legend(fontsize=7)

    fig.suptitle('Effect of price differentiation on outcomes', fontsize=11)
    fig.tight_layout()

    if save_to:
        fig.savefig(save_to, dpi=150, bbox_inches='tight')
    return fig


def plot_multiplicity(equilibria, params, save_to=None):
    """
    Show multiple equilibria found under uniform prices (wrong-equilibrium trap).
    Each equilibrium is one subplot showing frac_H per resort.
    """
    n = len(equilibria)
    if n == 0:
        print("  No multiplicity found -- single equilibrium.")
        return None

    fig, axes = plt.subplots(1, n, figsize=(3 * n, 3.5), sharey=True)
    if n == 1:
        axes = [axes]

    x = np.arange(params.n_resorts)
    for ax, eq, i in zip(axes, equilibria, range(n)):
        ax.bar(x, eq['frac_H'], color='#9B59B6', edgecolor='white', zorder=2)
        ax.axhline(params.N_H / params.N, color='gray', linestyle=':', linewidth=1.0)
        ax.set_xticks(x)
        ax.set_xticklabels(RESORT_LABELS)
        ax.set_ylim(0, 1)
        ax.set_title(f'Equilibrium {i+1}\nIV={eq["intrinsic"]:.3f}', fontsize=8)

    axes[0].set_ylabel('frac_H at resort')
    fig.suptitle(
        'Wrong-equilibrium trap: multiple QRE under uniform prices\n'
        '(high rationality, lam=15)',
        fontsize=10,
    )
    fig.tight_layout()

    if save_to:
        fig.savefig(save_to, dpi=150, bbox_inches='tight')
    return fig
