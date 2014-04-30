from framework.parameters.parameters import Parameters

__author__ = 'mhurson'


class DefaultTextBoxGraphicsParameters(Parameters):
    def __init__(self, topleft=(0, 0), dimensions=(150, 30),
                 bg_color=(255, 255, 255, 255)):
        self.topleft = topleft
        self.dimensions = dimensions
        self.bg_color = bg_color