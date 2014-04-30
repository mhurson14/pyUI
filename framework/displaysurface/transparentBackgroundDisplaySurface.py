import pygame
from framework.displaysurface.displaysurface import DisplaySurface

__author__ = 'mhurson'


class TransparentBackgroundDisplaySurface(DisplaySurface):
    def __init__(slef, params):
        super().__init__(params)

    def createSurface(self):
        kwargs = {}

        if self.flags:
            kwargs['flags'] = self.flags
        if self.depth:
            kwargs['depth'] = self.depth
        if self.masks:
            kwargs['masks'] = self.masks

        self.surface = pygame.Surface(self.dimensions, **kwargs)

        self.surface.set_colorkey((0,0,0))