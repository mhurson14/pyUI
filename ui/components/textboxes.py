import pygame
import ui
from pygame.locals import *

class DefaultTextBox(ui.textbox.TextBox):
    def __init__(self, topleft=(0,0), dimensions=(150,35),
                 background_color=(255,255,255,255),
                 text='', font_size=20, font_type=None,
                 font_color=(0, 0, 0, 255),
                 bold=False, italic=False, underline=False):

        text_size = ui.utils.getSizeOfText(text, font_size, font_type,
                                        bold, italic, underline)

        box_rect = pygame.Rect(0, 0, dimensions[0], dimensions[1])
        text_rect = pygame.Rect(0, 0, text_size[0], text_size[1])
        text_rect.left = 3
        text_rect.centery = box_rect.centery

        text_object = ui.text.SelectableText(None, ui.displaysurface.DisplaySurface,
                               ui.textgraphics.DefaultTextGraphics,
                               ui.parameters.DisplaySurfaceParameters(\
                                   dimensions=text_size,
                                   topleft=text_rect.topleft,
                                   flags=SRCALPHA),
                               ui.parameters.DefaultTextGraphicsParameters(\
                                   text=text,
                                   font_size=font_size,
                                   font_type=font_type,
                                   font_color=font_color,
                                   bold=bold,
                                   italic=italic,
                                   underline=underline))
        text_object.setVisible(True)
        
        super().__init__(None, ui.displaysurface.DisplaySurface,
                         ui.textboxgraphics.DefaultTextBoxGraphics,
                         ui.parameters.DisplaySurfaceParameters(\
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA),
                         ui.parameters.DefaultTextBoxGraphicsParameters(dimensions=dimensions),
                         text_object)
