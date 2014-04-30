from framework.parameters.parameters import Parameters

__author__ = 'mhurson'

class DisplaySurfaceParameters(Parameters):
    def __init__(self, dimensions=(100, 100), topleft=(0, 0),
                 flags=None, depth=None, masks=None):
        self.dimensions = dimensions
        self.topleft = topleft
        self.flags = flags
        self.depth = depth
        self.masks = masks