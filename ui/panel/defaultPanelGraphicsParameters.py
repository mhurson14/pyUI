from framework.parameters.parameters import Parameters

__author__ = 'mhurson'


class DefaultPanelGraphicsParameters(Parameters):
    def __init__(self, dimensions=(100, 100), topleft=(0, 0),
                 outline_width=1, border_width=12, buffer_width=0,
                 outline_color=(0, 0, 0), border_color=(255, 255, 255),
                 background_color=(100, 200, 100)):
        self.dimensions = dimensions
        self.topleft = topleft
        self.outline_width = outline_width
        self.border_width = border_width
        self.buffer_width = buffer_width
        self.outline_color = outline_color
        self.border_color = border_color
        self.background_color = background_color