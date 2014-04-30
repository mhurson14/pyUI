from framework.parameters.parameters import Parameters

__author__ = 'mhurson'


class DefaultCaretGraphicsParameters(Parameters):
    def __init__(self, topleft=(0, 0), dimensions=(1, 20),
                 color=(0, 0, 0, 255)):
        self.topleft = topleft
        self.dimensions = dimensions
        self.color = color