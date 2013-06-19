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
        self.image = None
        self.rect = None

        self.font = pygame.font.Font(self.font_type, self.font_size)

        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)
        self.font.set_underline(self.underline)

        self.image = self.font.render(self.text, True, self.font_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft
        self.dimensions = self.rect.size

    def getMetrics(self):
        return self.font.metrics(self.text)

    def draw(self, display_surface, area=None):
        display_surface.displayImage(self.image, self.rect, area)
