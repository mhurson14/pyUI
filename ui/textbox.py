from ui.uicomponent import *

class TextBox(FocusableUIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
