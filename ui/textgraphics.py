import pygame
from pygame import freetype
from pygame.locals import *
from ui import *

class DefaultTextGraphics:
    def __init__(self, params):

        self.text = params.text

        self.font_size = params.font_size
        self.font_type = params.font_type
        self.font_color = params.font_color

        #booleans
        self.bold = params.bold
        self.italic = params.italic
        self.underline = params.underline

        self.font = None

        self.dimensions = None
        self.topleft = params.topleft
        self.image_left = None
        self.image_selected = None
        self.image_right = None
        self.rect_left = None
        self.rect_selected = None
        self.rect_right = None

        self.font = pygame.font.Font(self.font_type, self.font_size)

        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)
        self.font.set_underline(self.underline)

        self.setSelected(0, 0)

        image = self.font.render(self.text, True, self.font_color)
        rect = image.get_rect()
        self.dimensions = rect.size

    def setSelected(self, start, end):

        self.image_left = None
        self.image_selected = None
        self.image_right = None
        self.rect_left = None
        self.rect_selected = None
        self.rect_right = None
        
        left = self.text[:start]
        selected = self.text[start:end]
        right = self.text[end:]
        metrics = self.getMetrics()
        if len(left) > 0:
            self.image_left = self.font.render(left, True, self.font_color)
            self.rect_left = self.image_left.get_rect()
            self.rect_left.topleft = self.topleft
        if len(selected) > 0:
            self.image_selected = self.font.render(selected, True,
                                                   (255, 255, 255, 255),
                                                   (150, 200, 150, 255))
            self.rect_selected = self.image_selected.get_rect()
            self.rect_selected.top = self.topleft[1]
            self.rect_selected.left = self.topleft[0]
            self.rect_selected.left += sum([metric[4] for metric in metrics[:start]])
        if len(right) > 0:
            self.image_right = self.font.render(right, True, self.font_color)
            self.rect_right = self.image_right.get_rect()
            self.rect_right.top = self.topleft[1]
            self.rect_right.left = self.topleft[0]
            self.rect_right.left += sum([metric[4] for metric in metrics[:end]])

    def getMetrics(self):
        return self.font.metrics(self.text)

    def draw(self, display_surface, area=None):
        if self.image_left:
            display_surface.displayImage(self.image_left, self.rect_left, area)
        if self.image_selected:
            display_surface.displayImage(self.image_selected, self.rect_selected, area)
        if self.image_right:
            display_surface.displayImage(self.image_right, self.rect_right, area)
        #display_surface.displayImage(self.image, self.rect, area)

























