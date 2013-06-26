import ui
from ui.uicomponent import *
from ui import internals
from pygame.locals import *

class TextBox(FocusableUIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text, caret=None):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.text = text
        self.addMember(self.text)

        self.valid_keys = {}

        self.left = K_LEFT
        self.right = K_RIGHT

        self.backspace = K_BACKSPACE
        self.delete = K_DELETE

        self.home = K_HOME
        self.end = K_END

        self.caret = caret
        if not self.caret:
            tl = (self.text.getHorizontalCoordinate(0),
                  self.display_surface.getRect().height // 2 - 10)
            self.caret = ui.caret.Caret(None, ui.displaysurface.DisplaySurface,
                                        ui.caretgraphics.DefaultCaretGraphics,
                                        ui.parameters.DisplaySurfaceParameters(\
                                            dimensions=(1, 20), topleft=tl,
                                            flags=SRCALPHA),
                                        ui.parameters.DefaultCaretGraphicsParameters(),
                                        self.text)
        self.addMember(self.caret)

        self.setValidKeys()

        self.caret_handler = ui.uiimplementers.CaretHandler(self.text, self.caret,
                                                            self.valid_keys)
        self.selecter = ui.uiimplementers.TextSelecter(self.text, self.caret)

        self.registerEvent(internals.KEYDOWNEVENT, self.onKeyPress)
        self.registerEvent(internals.MOUSEMOTIONEVENT, self.onMouseMove)

    def mouseOnePressCollide(self, event):
        super().mouseOnePressCollide(event)
        self.caret_handler.mouseOnePressCollide(event)
        self.selecter.mouseOnePressCollide(event)

    def pressedMouseMoveCollide(self, event):
        super().pressedMouseMoveCollide(event)
        self.caret_handler.pressedMouseMoveCollide(event)
        self.selecter.pressedMouseMoveCollide(event)

    def pressedMouseMoveMiss(self, event):
        super().pressedMouseMoveMiss(event)
        self.caret_handler.pressedMouseMoveMiss(event)
        self.selecter.pressedMouseMoveMiss(event)

    def pressedMouseOneReleaseCollide(self, event):
        super().pressedMouseOneReleaseCollide(event)
        self.selecter.pressedMouseOneReleaseCollide(event)

    def setFocus(self, val):
        super().setFocus(val)
        if val:
            self.addToDispatcher(internals.KEYDOWNEVENT)
            self.caret.setVisibleRecursive(True)
        else:
            self.removeFromDispatcher(internals.KEYDOWNEVENT)
            self.caret.setVisibleRecursive(False)

    def setValidKeys(self):
        for i in range(32, 127):
            self.valid_keys[chr(i)] = i

    def drawMembers(self):
        self.text.draw()
        self.caret.draw()

    def onKeyPress(self, event):
        if self.hasFocus():
            if event.unicode in self.valid_keys:
                self.text.insertText(event.unicode, self.caret.getPosition())
            elif event.key == self.backspace:
                start = self.text.getSelectionStart()
                end = self.text.getSelectionEnd()
                if start == end:
                    self.text.deleteCharacter(self.caret.getPosition() - 1)
                else:
                    self.text.deleteText(start, end - 1)
            elif event.key == self.delete:
                start = self.text.getSelectionStart()
                end = self.text.getSelectionEnd()
                if start == end:
                    self.text.deleteCharacter(self.caret.getPosition())
                else:
                    self.text.deleteText(start, end - 1)

            self.caret_handler.onKeyPress(event)
            self.selecter.onKeyPress(event)













