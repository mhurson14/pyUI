from ui.component.uicomponent import *
from ui.displaysurface import displaysurface

class Screen(UIComponent):
    def __init__(self):

        super().__init__(None, displaysurface.ScreenSurface,
                         ui.graphics.nullgraphics.NullGraphics, None, None)

        self.setVisible(True)

    def getAbsoluteRect(self):
        return pygame.display.get_surface().get_rect()

    def getVisible(self):
        return self.visible
