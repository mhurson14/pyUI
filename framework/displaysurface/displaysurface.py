import pygame


class DisplaySurface:
    def __init__(self, params):

        self.params = params
        
        self.dimensions = params.dimensions
        self.topleft = params.topleft

        self.flags = params.flags
        self.depth = params.depth
        self.masks = params.masks
        
        self.surface = None
        self.rect = None

        self.createSurface()
        self.createRect()

    def createSurface(self):

        kwargs = {}
        
        if self.flags:
            kwargs['flags'] = self.flags
        if self.depth:
            kwargs['depth'] = self.depth
        if self.masks:
            kwargs['masks'] = self.masks

        self.surface = pygame.Surface(self.dimensions, **kwargs)

    def createRect(self):
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.topleft

    def setDimensions(self, dimensions):
        self.dimensions = dimensions
        self.createSurface()
        self.createRect()

    def setTopleft(self, topleft):
        self.topleft = topleft
        self.rect.topleft = topleft

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












