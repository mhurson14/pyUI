from pygame.locals import *

from framework.displaysurface import displaysurface
from framework.displaysurface.screenSurface import ScreenSurface
from framework.graphics import nullGraphics
from framework.parameters.displaySurfaceParameters import DisplaySurfaceParameters
from ui.menu import menu


class DefaultMenu(menu.Menu):
    def __init__(self, parent=None, topleft=(0, 0), dimensions=(100, 100)):

        super().__init__(parent, displaysurface.DisplaySurface,
                         nullGraphics.NullGraphics,
                         DisplaySurfaceParameters(
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA), None)

        #self.nullsurf = displaysurface.NullSurface()
        self.screen_surf = ScreenSurface()

    '''def draw(self):
        super().draw(self.screen_surf)'''

    '''def draw(self):
        super().draw(self.nullsurf)'''
