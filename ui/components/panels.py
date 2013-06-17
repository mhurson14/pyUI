from ui import *
from pygame.locals import *

class DefaultPanel(panel.Panel):
    def __init__(self, dimensions=(100, 100), topleft=(0, 0),
                 outline_width=1, border_width=12, buffer_width=0,
                 outline_color=(0, 0, 0), border_color=(255, 255, 255),
                 background_color=(100, 200, 100)):

        super().__init__(None, displaysurface.DisplaySurface,
                         panelgraphics.DefaultPanelGraphics,
                         parameters.DisplaySurfaceParameters(\
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA),
                         parameters.DefaultPanelGraphicsParameters(\
                             dimensions=dimensions,
                             outline_width=outline_width,
                             border_width=border_width,
                             buffer_width=buffer_width,
                             outline_color=outline_color,
                             border_color=border_color,
                             background_color=background_color))
