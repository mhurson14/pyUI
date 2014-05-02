from pygame.locals import *

from framework.displaysurface import displaysurface
from framework.parameters.displaySurfaceParameters import DisplaySurfaceParameters
from ui.text import text as t, textGraphics
from ui import utils
from ui.text.defaultTextGraphicsParameters import DefaultTextGraphicsParameters


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
                         textGraphics.DefaultTextGraphics,
                         DisplaySurfaceParameters(
                             dimensions=text_size,
                             topleft=topleft,
                             flags=SRCALPHA),
                         DefaultTextGraphicsParameters(
                             text=text,
                             dimensions=text_size,
                             font_size=font_size,
                             font_type=font_type,
                             font_color=font_color,
                             bold=bold,
                             italic=italic,
                             underline=underline))


