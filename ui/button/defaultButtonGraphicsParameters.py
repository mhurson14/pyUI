from framework.parameters.parameters import Parameters

__author__ = 'mhurson'


class DefaultButtonGraphicsParameters(Parameters):
    def __init__(self, topleft=(0,0), dimensions=(100,40),
                 color=(180, 180, 180), highlight_color=None):
        self.topleft = topleft
        self.dimensions = dimensions
        self.color = color
        self.highlight_color = highlight_color