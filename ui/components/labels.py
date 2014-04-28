import ui
from pygame.locals import *

class DefaultLabel(ui.text.Text):
    def __init__(self, text='', topleft=(0,0), width=144, font_size=20,
                 font_type='/usr/share/fonts/truetype/freefont/FreeSans.ttf',
                 font_color=(255,255,255,255),
                 bold=False, italic=False, underline=False):

        text_size = ui.utils.getSizeOfText(text, font_size, font_type,
                                        bold, italic, underline)

        dimensions = (width, ui.utils.getTextHeight(font_size, font_type,
                                                    bold, italic, underline))

        super().__init__(None, ui.displaysurface.DisplaySurface,
                               ui.textgraphics.DefaultTextGraphics,
                               ui.parameters.DisplaySurfaceParameters(\
                                   dimensions=text_size,
                                   topleft=topleft,
                                   flags=SRCALPHA),
                               ui.parameters.DefaultTextGraphicsParameters(\
                                   text=text,
                                   dimensions=dimensions,
                                   font_size=font_size,
                                   font_type=font_type,
                                   font_color=font_color,
                                   bold=bold,
                                   italic=italic,
                                   underline=underline))
