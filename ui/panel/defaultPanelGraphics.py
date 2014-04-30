import pygame

class DefaultPanelGraphics:
    def __init__(self, params):

        self.dimensions = params.dimensions
        self.topleft = params.topleft

        self.outline_width = params.outline_width
        self.border_width = params.border_width
        self.buffer_width = params.buffer_width

        self.outline_color = params.outline_color
        self.border_color = params.border_color
        self.background_color = params.background_color

        self.flags = pygame.locals.SRCALPHA

        #This will display the outline of the panel
        self.outline_surf = pygame.Surface(self.dimensions, flags=self.flags)
        self.outline_surf.fill(self.outline_color)
        self.outline_rect = self.outline_surf.get_rect()
        self.outline_rect.topleft = self.topleft

        
        #This will display the border of the panel
        self.border_surf = pygame.Surface(
            (self.dimensions[0] - 2 * self.outline_width,
             self.dimensions[1] - 2 * self.outline_width), flags=self.flags)
        self.border_surf.fill(self.border_color)
        self.border_rect = self.border_surf.get_rect()
        self.border_rect.topleft = (self.outline_rect.left + self.outline_width,
                                    self.outline_rect.top + self.outline_width)

        #This will display the background of the panel
        self.background_surf = pygame.Surface(
            (self.border_rect.width - 2 * self.border_width,
             self.border_rect.height - 2 * self.border_width), flags=self.flags)
        self.background_surf.fill(self.background_color)
        self.background_rect = self.background_surf.get_rect()
        self.background_rect.topleft =\
            (self.border_rect.left + self.border_width,
             self.border_rect.top + self.border_width)

    def draw(self, display_surface, area=None):
        display_surface.displayImage(self.outline_surf, self.outline_rect, area)
        display_surface.displayImage(self.border_surf, self.border_rect, area)
        display_surface.displayImage(self.background_surf, self.background_rect, area)
