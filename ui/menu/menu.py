from ui.component.uicomponent import *

class Menu(UIContainer):
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

    def calculateAbsoluteRect(self):
        self.absolute_rect = self.display_surface.getRect()
