import pygame
from ui.uicomponent import *

class Text(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text=''):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.text = text
