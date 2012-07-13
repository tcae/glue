# Define acceptable line styles
VALID_LINESTYLES = ['solid', 'dashed', 'dash-dot', 'dotted', 'none']

GREY = '#B2B2B2'
GRAY = GREY
BLUE = "#1F7884"
GREEN = "#33A02C"
RED = "#E31A1C"
ORANGE = "#FF7F00"
PURPLE = "#6A3D9A"
LIGHT_BLUE = "#A6CEE3"
LIGHT_GREEN = "#B2DF8A"
LIGHT_RED = "#FB9A99"
LIGHT_ORANGE = "#FDBF6F"
LIGHT_PURPLE = "#CAB2D6"

__all__ = ['VisualAttributes']


class VisualAttributes(object):
    '''
    This class is used to define visual attributes for any kind of objects
    '''

    def __init__(self, parent=None, washout=False, color=GREY):

        # Color can be specified using Matplotlib notation. Specifically, it
        # can be:
        #  * A string with a common color (e.g. 'black', 'red', 'orange')
        #  * A string containing a float in the rng [0:1] for a shade of
        #    gray ('0.0' = black,'1.0' = white)
        #  * A tuple of three floats in the rng [0:1] for (R, G, B)
        #  * An HTML hexadecimal string (e.g. '#eeefff')
        self.color = color
        self.alpha = 1.

        # Line width in points (float or int)
        self.linewidth = 1

        # Line style, which can be one of 'solid', 'dashed', 'dash-dot',
        # 'dotted', or 'none'
        self.linestyle = 'solid'

        self.marker = 'o'
        self.markersize = 40
        self.label = None

        self.parent = parent

    def set(self, other):
        self.color = other.color
        self.alpha = other.alpha
        self.linewidth = other.linewidth
        self.linestyle = other.linestyle
        self.marker = other.marker
        self.markersize = other.markersize

    def __setattr__(self, attribute, value):

        # Check that line style is valid
        if attribute == 'linestyle' and value not in VALID_LINESTYLES:
            raise Exception("Line style should be one of %s" %
                            '/'.join(VALID_LINESTYLES))

        # Check that line width is valid
        if attribute == 'linewidth':
            if type(value) not in [float, int]:
                raise Exception("Line width should be a float or an int")
            if value < 0:
                raise Exception("Line width should be positive")

        # Check that the attribute exists (don't allow new attributes)
        allowed = set(['color', 'linewidth', 'linestyle',
                       'alpha', 'parent', 'marker', 'markersize', 'label'])
        if attribute not in allowed:
            raise Exception("Attribute %s does not exist" % attribute)

        object.__setattr__(self, attribute, value)

        # if parent has a broadcast method, broadcast the change
        if hasattr(self, 'parent') and hasattr(self.parent, 'broadcast'):
            self.parent.broadcast(self)
