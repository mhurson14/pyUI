import pygame
import ui
from mydraw import shapes
from mydraw import fill
from pygame.locals import *

class DefaultTextBoxGraphics:
    def __init__(self, params):

        self.topleft = params.topleft
        self.dimensions = params.dimensions

        self.image = None
        self.rect = None

        self.bg_color = params.bg_color

        self.generateImage()

        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft

    def generateImage(self):

        colors = [(128, 128, 128, 200), (128, 128, 128, 255)]
        

        #radius = int(self.dimensions[1] / 5)
        radius = 0

        self.image = pygame.Surface(self.dimensions, flags=SRCALPHA)
        back_color = (100, 100, 100, 0)
        self.image.fill(back_color)
        
        self.image = shapes.drawRoundedRect(\
            self.dimensions[0] - 2 * radius,
            self.dimensions[1] - 2 * radius,
            radius, colors, 2, surface = self.image)

        fill.fillSolid(self.image, self.bg_color, 2, self.dimensions[1] - 3,
                       bg_color = back_color)

    def draw(self, display_surface, area=None):
        display_surface.displayImage(self.image, self.rect, area)
