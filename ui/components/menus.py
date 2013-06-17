from ui import *
from pygame.locals import *

class DefaultMenu(menu.Menu):
    def __init__(self, parent=None, topleft=(0, 0), dimensions=(100, 100)):

        super().__init__(parent, displaysurface.DisplaySurface,
                         nullgraphics.NullGraphics,
                         parameters.DisplaySurfaceParameters(\
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA), None)

        #self.nullsurf = displaysurface.NullSurface()
        self.screen_surf = displaysurface.ScreenSurface()

    '''def draw(self):
        super().draw(self.screen_surf)'''

    '''def draw(self):
        super().draw(self.nullsurf)'''
