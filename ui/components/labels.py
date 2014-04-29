from pygame.locals import *

from ui.displaysurface import displaysurface
from ui.text import text as t, textgraphics
from ui import parameters
from ui import utils


class DefaultLabel(t.Text):
    def __init__(self, text='', topleft=(0, 0), width=144, font_size=20,
                 font_type='/usr/share/fonts/truetype/freefont/FreeSans.ttf',
                 font_color=(255, 255, 255, 255),
                 bold=False, italic=False, underline=False):
        text_size = utils.getSizeOfText(text, font_size, font_type,
                                        bold, italic, underline)

        dimensions = (width, utils.getTextHeight(font_size, font_type,
                                                 bold, italic, underline))

        super().__init__(None, displaysurface.DisplaySurface,
                         textgraphics.DefaultTextGraphics,
                         parameters.DisplaySurfaceParameters(
                             dimensions=text_size,
                             topleft=topleft,
                             flags=SRCALPHA),
                         parameters.DefaultTextGraphicsParameters(
                             text=text,
                             dimensions=text_size,
                             font_size=font_size,
                             font_type=font_type,
                             font_color=font_color,
                             bold=bold,
                             italic=italic,
                             underline=underline))
