import matplotlib.pyplot as plt

def default():
    plt.style.use('default')
    return None

def style(serif='Computer Modern'):
    """ Use custom config."""
    plt.style.use('seaborn-whitegrid')
    config = {
        'text.usetex': True,    # use LaTeX to render text
        'font.family': 'serif',
        'font.serif': [serif],
        'figure.constrained_layout.use': True,
        'legend.frameon': True,
        'legend.edgecolor': 'none',
    }
    plt.rcParams.update(config)
    return None

