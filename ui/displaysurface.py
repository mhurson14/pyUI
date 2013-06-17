import pygame
from pygame.locals import *
from ui.parameters import *

class DisplaySurface:
    def __init__(self, params):

        self.params = params
        
        self.dimensions = params.dimensions
        self.topleft = params.topleft
        
        self.surface = None
        self.rect = None

        self.createSurface(params)

        self.rect = self.surface.get_rect()
        self.rect.topleft = self.topleft

    def createSurface(self, params):

        kwargs = {}
        
        if params.flags:
            kwargs['flags'] = params.flags
        if params.depth:
            kwargs['depth'] = params.depth
        if params.masks:
            kwargs['masks'] = params.masks

        self.surface = pygame.Surface(params.dimensions, **kwargs)

    def getRect(self):
        return self.rect

    def getSurface(self):
        return self.surface

    def clear(self):
        self.surface.fill((0, 0, 0, 0))

    #Used to draw pygame surfaces to this surface
    def displayImage(self, surf, rect, area=None):
        ''' Draw pygame surfaces to this surface.
        Params the same as pygame.Surface.blit()'''
        
        self.surface.blit(surf, rect, area)

    #Used to draw other DisplaySurfaces onto this surface
    def displaySurface(self, surf, area=None):
        '''Draw other DisplaySurfaces to this surface.'''

        self.surface.blit(surf.getSurface(), surf.getRect(), area)

class TransparentBackgroundDisplaySurface(DisplaySurface):
    def __init__(slef, params):
        super().__init__(params)

    def createSurface(self, params):
        kwargs = {}
        
        if params.flags:
            kwargs['flags'] = params.flags
        if params.depth:
            kwargs['depth'] = params.depth
        if params.masks:
            kwargs['masks'] = params.masks

        self.surface = pygame.Surface(params.dimensions, **kwargs)

        self.surface.set_colorkey((0,0,0))

class ScreenSurface(DisplaySurface):
    def __init__(self, params=None):

        params = DisplaySurfaceParameters(pygame.display.get_surface().get_rect().size,
                                          (0, 0))
        
        super().__init__(params)

    def createSurface(self, params):
        self.surface = pygame.display.get_surface()

class NullSurface:
    def __init__(self):
        pass

    def displaySurface(self, surf, area=None):
        pass

    def clear(self):
        pass












