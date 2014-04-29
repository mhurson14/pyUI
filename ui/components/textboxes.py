import pygame
from pygame.locals import *
from ui.text import textbox, textboxgraphics, textgraphics, text as t
from ui.displaysurface import displaysurface
from ui import parameters
from ui import utils


class DefaultTextBox(textbox.TextBox):
    def __init__(self, topleft=(0, 0), dimensions=(150, 35),
                 background_color=(255, 255, 255, 255),
                 text='', font_size=20, font_type=None,
                 font_color=(0, 0, 0, 255),
                 bold=False, italic=False, underline=False):
        '''text_size = ui.utils.getSizeOfText(text, font_size, font_type,
                                        bold, italic, underline)'''

        height = utils.getTextHeight(font_size, font_type, bold, italic, underline)

        box_rect = pygame.Rect(0, 0, dimensions[0], dimensions[1])
        text_rect = pygame.Rect(0, 0, dimensions[0] - 8, height)
        text_rect.left = 3
        text_rect.centery = box_rect.centery

        text_object = t.SelectableText(None, displaysurface.DisplaySurface,
                                       textgraphics.DefaultTextGraphics,
                                       parameters.DisplaySurfaceParameters(
                                           dimensions=text_rect.size,
                                           topleft=text_rect.topleft,
                                           flags=SRCALPHA),
                                       parameters.DefaultTextGraphicsParameters(
                                           text=text,
                                           dimensions=text_rect.size,
                                           font_size=font_size,
                                           font_type=font_type,
                                           font_color=font_color,
                                           bold=bold,
                                           italic=italic,
                                           underline=underline))
        text_object.setVisible(True)

        super().__init__(None, displaysurface.DisplaySurface,
                         textboxgraphics.DefaultTextBoxGraphics,
                         parameters.DisplaySurfaceParameters(
                             dimensions=dimensions,
                             topleft=topleft,
                             flags=SRCALPHA),
                         parameters.DefaultTextBoxGraphicsParameters(dimensions=dimensions),
                         text_object)
