import ui
from ui.uicomponent import *

class Screen(UIComponent):
    def __init__(self):

        super().__init__(None, ui.displaysurface.ScreenSurface,
                         ui.nullgraphics.NullGraphics, None, None)

        self.setVisible(True)

    def getAbsoluteRect(self):
        return pygame.display.get_surface().get_rect()

    def getVisible(self):
        return self.visible
