from ui.uicomponent import *
from ui import internals
from ui import eventtimer
from ui import uievent

class Caret(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params,
                 text, blink_delay=700, pos=0):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.text = text

        self.position = pos

        self.blink_delay = blink_delay

        self.registerEvent(internals.CARETTIMEREVENT, self.onBlink)

        blink_timer = eventtimer.EventTimer(uievent.CaretBlinkEvent(self).getEvent(),
                                            self.blink_delay)
        self.registerTimer(blink_timer)

    def onBlink(self, event):
        if event.caret == self:
            self.graphics.setDisplay(not self.graphics.getDisplay())

    def setVisible(self, val):
        super().setVisible(val)
        if val:
            self.graphics.setDisplay(True)

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
