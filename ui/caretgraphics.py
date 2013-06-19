import ui
import pygame

class DefaultCaretGraphics:
    def __init__(self, params):

        self.topleft = params.topleft
        self.dimensions = params.dimensions

        self.color = params.color

        self.image = pygame.Surface(self.dimensions)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.topleft

    def draw(self, display_surface, area=None):
        display_surface.displayImage(self.image, self.rect, area)
