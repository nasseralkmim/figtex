import matplotlib as mpl

def default():
    mpl.style.use('default')
    return None

def style(typeface='DejaVu Serif'):
    """ Use custom config."""
    default()
    config = {
        'text.usetex': True,    # use LaTeX to render text
        'font.family': 'serif',
    }
    mpl.rcParams.update(config)
    return None

