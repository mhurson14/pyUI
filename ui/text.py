import pygame
from ui.uicomponent import *
import ui.utils
import time

class Text(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text=''):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.text = text

    def getEnd(self):
        return len(self.text)

    def getClickedPosition(self, coord):
        rect = self.getAbsoluteRect()
        if rect.collidepoint(coord):
            rects = self.getAbsoluteCharacterRects()
            #print(rects)
            for i in range(len(rects)):
                char_rect = rects[i]
                if char_rect.collidepoint(coord):
                    if coord[0] <= char_rect.centerx:
                        return i
                    else:
                        return i + 1
            return len(rects)
        else:
            return None

    def getViewRect(self):
        return self.graphics.getRect()

    def setViewRect(self, rect):
        self.graphics.setRect(rect)

    def getRelativeCharacterRect(self, position):
        rect = self.getRelativeRect()
        top = rect.top
        left = rect.left
        metrics = self.graphics.getMetrics()
        for i in range(position):
            left += metrics[i][4]
        height = rect.height
        width = metrics[position][4] - metrics[position][0]
        result = pygame.Rect(left, top, width + 1, height)
        return result

    def getAbsoluteCharacterRect(self, position):
        rect = self.getAbsoluteRect()
        top = rect.top
        left = rect.left
        metrics = self.graphics.getMetrics()
        for i in range(position):
            left += metrics[i][4]
        height = rect.height
        width = metrics[position][4] - metrics[position][0]
        result = pygame.Rect(left, top, width + 1, height)
        result.left -= self.getViewRect().left
        return result

    def getAbsoluteCharacterRects(self):
        rect = self.getAbsoluteRect()
        results = []
        metrics = self.graphics.getMetrics()
        advance = 0
        for i in range(len(self.text)):
            left = rect.left + advance
            top = rect.top
            width = metrics[i][4] - metrics[i][0]
            height = rect.height
            result = pygame.Rect(left, top, width + 1, height)
            result.left -= self.getViewRect().left
            results.append(result)
            advance += metrics[i][4]
        return results

    def getHorizontalCoordinate(self, position):
        if position >= 0 and position <= len(self.text):
            result = self.getRelativeRect().left
            result -= self.getViewRect().left
            if position > 0:
                metrics = self.graphics.getMetrics()
                if position <= len(metrics):
                    result += sum([metric[4] for metric in metrics[:position]])
            return result

    def getAbsoluteHorizontalCoordinate(self, position):
        return self.getAbsoluteRect().left + self.getHorizontalCoordinate(position)

    def insertText(self, text, index):
        newText = self.text[:index] + text + self.text[index:]
        self.setText(newText)

    def deleteText(self, start, end):
        if start <= end and start >= 0 and end <= len(self.text):
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

        '''size = ui.utils.getSizeOfText(self.text, self.graphics_params.font_size,
                                      self.graphics_params.font_type,
                                      self.graphics_params.bold,
                                      self.graphics_params.italic,
                                      self.graphics_params.underline)'''

        #self.surface_params.dimensions = size
        #self.display_surface = self.surface_type(self.surface_params)

        self.graphics = self.graphics_type(self.graphics_params)

    def getText(self):
        return self.text

    def __len__(self):
        return len(self.text)

class SelectableText(Text):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text=''):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.selection_start = 0
        self.selection_end = 0

    def setSelected(self, start, end):
        self.selection_start = start
        self.selection_end = end

        self.graphics.setSelected(start, end)

    def getSelectionStart(self):
        return self.selection_start

    def getSelectionEnd(self):
        return self.selection_end














