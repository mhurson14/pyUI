import pygame
from ui.uicomponent import *
import ui.utils

class Text(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text=''):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.text = text

    def getHorizontalCoordinate(self, position):
        if position >= 0 and position <= len(self.text):
            result = self.getRelativeRect().left
            if position > 0:
                metrics = self.graphics.getMetrics()
                if position <= len(metrics):
                    result += sum([metric[4] for metric in metrics[:position]])
            return result

    def insertText(self, text, index):
        newText = self.text[:index] + text + self.text[index:]
        self.setText(newText)

    def deleteText(self, start, end):
        if start <= end and start >= 0 and end < len(self.text):
            newText = self.text[:start] + self.text[end + 1:]
            self.setText(newText)
        else:
            raise Exception('Invalid indices')

    def deleteCharacter(self, index):
        if index >= 0:
            newText = self.text[:index] + self.text[index + 1:]
            self.setText(newText)

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

    def __len__(self):
        return len(self.text)














