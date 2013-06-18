from ui.uicomponent import *

class Caret(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params,
                 text, pos=0):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.text = text

        self.pos = pos
