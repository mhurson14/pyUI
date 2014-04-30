import pygame
from pygame.locals import *

from framework.displaysurface import displaysurface
from framework.parameters.displaySurfaceParameters import DisplaySurfaceParameters
from ui.button import button, buttonGraphics
from ui.button.defaultButtonGraphicsParameters import DefaultButtonGraphicsParameters
from ui.text import text, textGraphics
from ui.text.defaultTextGraphicsParameters import DefaultTextGraphicsParameters


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
                               textGraphics.DefaultTextGraphics,
                               DisplaySurfaceParameters(
                                   dimensions=text_rect.size,
                                   topleft=text_rect.topleft,
                                   flags=SRCALPHA),
                               DefaultTextGraphicsParameters(
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
                         buttonGraphics.DefaultButtonGraphics,
                         DisplaySurfaceParameters(
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA),
                         DefaultButtonGraphicsParameters(
                             dimensions = dimensions,
                             color = color,
                             highlight_color = highlight_color),
                         textObject)
        
