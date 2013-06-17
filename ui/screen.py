import ui
from ui.uicomponent import *

class Screen(UIComponent):
    def __init__(self):

        super().__init__(None, ui.displaysurface.ScreenSurface,
                         ui.nullgraphics.NullGraphics, None, None)
