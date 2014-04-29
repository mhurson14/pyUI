from ui.event import eventtimer, uievent
from ui.component.uicomponent import *


class Caret(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params,
                 text, blink_delay=700, pos=0):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.text = text

        self.text_scroller = ui.uiimplementers.TextScroller(self.text)

        self.position = pos

        self.blink_delay = blink_delay

        self.blink_timer = eventtimer.EventTimer(uievent.CaretBlinkEvent(self).getEvent(),
                                            self.blink_delay)

        self.registerEvent(ui.internals.CARETTIMEREVENT, self.onBlink)

        self.registerTimer(self.blink_timer)

    def onBlink(self, event):
        if event.caret == self:
            self.graphics.setDisplay(not self.graphics.getDisplay())

    def setVisible(self, val):
        super().setVisible(val)
        if val:
            self.graphics.setDisplay(True)

    def getPosition(self):
        return self.position

    def getLeft(self):
        return self.display_surface.getRect().left

    def setLocation(self, position):
        if position >= 0 and position <= len(self.text):
            self.text_scroller.onSetLocation(position)
            x = self.text.getHorizontalCoordinate(position)
            y = self.parent.getRelativeRect().height // 2 -\
                self.getRelativeRect().height // 2
            self.display_surface.setTopleft((x, y))
            self.position = position
        self.graphics.setDisplay(True)

    def moveLeft(self):
        self.setLocation(self.position - 1)

    def moveRight(self):
        self.setLocation(self.position + 1)











