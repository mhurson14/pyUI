from framework.parameters.parameters import Parameters

__author__ = 'mhurson'


class DefaultTextGraphicsParameters(Parameters):
    def __init__(self, text='', topleft=(0, 0), dimensions=(144, 20),
                 font_size=14, font_type=None,
                 font_color=(255, 255, 255, 255),
                 bold=False, italic=False, underline=False):
        self.text = text
        self.topleft = topleft
        self.dimensions = dimensions
        self.font_size = font_size
        self.font_type = font_type
        self.font_color = font_color
        self.bold = bold
        self.italic = italic
        self.underline = underline