import pygame
from ui.uicomponent import *
import ui.utils

class Text(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text=''):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.text = text

    def setText(self, text):
        self.text = text

        self.graphics_params.text = self.text

        size = ui.utils.getSizeOfText(self.text, self.graphics_params.font_size,
                                      self.graphics_params.font_type,
                                      self.graphics_params.bold,
                                      self.graphics_params.italic,
                                      self.graphics_params.underline)

        self.surface_params.dimensions = size
        self.display_surface = self.surface_type(self.surface_params)

        self.graphics = self.graphics_type(self.graphics_params)

    def getText(self):
        return self.text
