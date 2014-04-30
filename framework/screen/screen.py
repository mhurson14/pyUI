import pygame

from framework.displaysurface.screenSurface import ScreenSurface
from framework.graphics import nullGraphics
from framework.object.baseobject import BaseObject


class Screen(BaseObject):
    def __init__(self):

        super().__init__(None, ScreenSurface,
                         nullGraphics.NullGraphics, None, None)

        self.setVisible(True)

    def getAbsoluteRect(self):
        return pygame.display.get_surface().get_rect()

    def getVisible(self):
        return self.visible
