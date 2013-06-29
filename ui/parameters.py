class Parameters:
    def __init__(self):
        pass

class DisplaySurfaceParameters(Parameters):
    def __init__(self, dimensions=(100, 100), topleft=(0, 0),
                 flags=None, depth=None, masks=None):
        self.dimensions = dimensions
        self.topleft = topleft
        self.flags = flags
        self.depth = depth
        self.masks = masks

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

class DefaultButtonGraphicsParameters(Parameters):
    def __init__(self, topleft=(0,0), dimensions=(100,40),
                 color=(180, 180, 180), highlight_color=None):
        self.topleft = topleft
        self.dimensions = dimensions
        self.color = color
        self.highlight_color = highlight_color

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

class DefaultTextBoxGraphicsParameters(Parameters):
    def __init__(self, topleft=(0, 0), dimensions=(150, 30),
                 bg_color=(255, 255, 255, 255)):
        self.topleft = topleft
        self.dimensions = dimensions
        self.bg_color = bg_color

class DefaultCaretGraphicsParameters(Parameters):
    def __init__(self, topleft=(0, 0), dimensions=(1, 20),
                 color=(0, 0, 0, 255)):
        self.topleft = topleft
        self.dimensions = dimensions
        self.color = color




















