import pygame
from ui import *
from pygame.locals import *


class DefaultButton(button.Button):
    def __init__(self, topleft=(0,0), dimensions=(100,40),
                 color=(180, 180, 180), highlight_color=None,
                 text_in='', font_size=20, font_type=None,
                 font_color=(255,255,255,255),
                 bold=False, italic=False, underline=False):

        button_rect = pygame.Rect(0, 0, dimensions[0], dimensions[1])
        text_rect = pygame.Rect(0, 0, dimensions[0] - 10, dimensions[1] - 10)
        text_rect.center = button_rect.center
        text_rect.top += 1

        textObject = text.Text(None, displaysurface.DisplaySurface,
                               textgraphics.DefaultTextGraphics,
                               parameters.DisplaySurfaceParameters(\
                                   dimensions=text_rect.size,
                                   topleft=text_rect.topleft,
                                   flags=SRCALPHA),
                               parameters.DefaultTextGraphicsParameters(\
                                   text=text_in,
                                   dimensions=text_rect.size,
                                   font_size=font_size,
                                   font_type=font_type,
                                   font_color=font_color,
                                   bold=bold,
                                   italic=italic,
                                   underline=underline))
        
        textObject.setVisible(True)
        
        super().__init__(None, displaysurface.DisplaySurface,
                         buttongraphics.DefaultButtonGraphics,
                         parameters.DisplaySurfaceParameters(\
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA),
                         parameters.DefaultButtonGraphicsParameters(\
                             dimensions = dimensions,
                             color = color,
                             highlight_color = highlight_color),
                         textObject)
        
