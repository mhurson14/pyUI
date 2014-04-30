import pygame
from framework.displaysurface.displaysurface import DisplaySurface
from framework.parameters.displaySurfaceParameters import DisplaySurfaceParameters

__author__ = 'mhurson'


class ScreenSurface(DisplaySurface):
    def __init__(self, params=None):

        params = DisplaySurfaceParameters(pygame.display.get_surface().get_rect().size,
                                          (0, 0))

        super().__init__(params)

    def createSurface(self):
        self.surface = pygame.display.get_surface()