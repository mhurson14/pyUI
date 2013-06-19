from ui.uicomponent import *

class Caret(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params,
                 text, pos=0):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.text = text

        self.position = pos

    def getPosition(self):
        return self.position

    def setLocation(self, position):
        if position >= 0 and position <= len(self.text):
            x = self.text.getHorizontalCoordinate(position)
            y = self.parent.getRelativeRect().height // 2 -\
                self.getRelativeRect().height // 2
            self.display_surface.setTopleft((x, y))
            self.position = position

    def moveLeft(self):
        self.setLocation(self.position - 1)

    def moveRight(self):
        self.setLocation(self.position + 1)
