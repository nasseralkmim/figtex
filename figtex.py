import matplotlib.pyplot as plt
import matplotlib as mpl

def default():
    plt.style.use('default')
    return None

def style(serif='Computer Modern'):
    """ Use custom config."""
    config = {
        'text.usetex': True,    # use LaTeX to render text
        'font.family': 'serif',
        'font.serif': [serif]
    }
    mpl.rcParams.update(config)
    return None
