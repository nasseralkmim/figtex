"""Nasser's default plot style."""
import matplotlib.pyplot as plt
import itertools

markers = itertools.cycle(('o', 'P', 's', 'X', '^', 'x'))
linestyles = itertools.cycle(('-', '--', '-.', ':'))

def default():
    """Make it matplotlib's default."""
    plt.style.use('default')
    return None


def style(serif='Computer Modern'):
    """Set custom config."""
    try:
        plt.style.use('fivethirtyeight')
    except OSError:
        # if matplotlib version does not have the style
        pass
    config = {
        # 'text.usetex': True,    # use LaTeX to render text
        # 'font.family': 'serif',
        # 'font.serif': [serif],
        # 'figure.constrained_layout.use': True,
        'svg.fonttype': 'none',
        # 'figure.autolayout': True, # auto adjust subplots
        'legend.frameon': True,
        'legend.edgecolor': 'none',
        'legend.fontsize': 8,
        'legend.framealpha': .3,
        'font.size': 10.0,
        'axes.grid': True,
        'axes.axisbelow': True,
        # frame: fivethirtyeight paints the spines the same color as the
        # background, so set an explicit edge color to make them show up.
        # Same gray as the grid, so the frame reads as part of it
        'axes.edgecolor': '0.78',
        'axes.linewidth': 0.5,
        # grid: keep the contrast in the color, not in the alpha, so it does
        # not depend on whatever is drawn behind it
        'grid.color': '0.78',
        'grid.alpha': 1.0,
        'grid.linewidth': 0.5,
        # no tick marks, only the frame and the labels
        'xtick.major.size': 0,
        'ytick.major.size': 0,
        'xtick.minor.size': 0,
        'ytick.minor.size': 0,
        'lines.linewidth': 0.5,   # default is 1.5
        # 'lines.markerfacecolor': "white",
        'lines.markeredgewidth': 0.5,
        'text.latex.preamble': r"\usepackage{amsmath}",  # allows \text in math env
    }
    plt.rcParams.update(config)
    return None
