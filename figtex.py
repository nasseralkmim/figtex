"""Nasser's default plot style."""
import matplotlib.pyplot as plt


def default():
    """Make it matplotlib's default."""
    plt.style.use('default')
    return None


def style(serif='Computer Modern'):
    """Set custom config."""
    plt.style.use('seaborn-colorblind')
    config = {
        'text.usetex': True,    # use LaTeX to render text
        'font.family': 'serif',
        'font.serif': [serif],
        # 'figure.constrained_layout.use': True,
        'legend.frameon': True,
        'legend.edgecolor': 'none',
        'legend.fontsize': 8,
        'font.size': 10.0,
        'axes.grid': True,
        'axes.linewidth': 1,    # seaborn changed to a ticker, better 1
        'axes.edgecolor': '0.8',
        'grid.color': '0.8',
        'text.color': '0.15',
        'xtick.color': '0.15',
        'ytick.color': '0.15',
        'lines.linewidth': 1,   # default is 1.5
        'text.latex.preamble': r"\usepackage{amsmath}", # allows \text in math env
    }
    plt.rcParams.update(config)
    return None

