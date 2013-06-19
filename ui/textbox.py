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

        self.registerEvent(internals.KEYDOWNEVENT, self.onKeyPress)

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
                self.caret.moveRight()
            elif event.key == self.backspace:
                self.text.deleteCharacter(self.caret.getPosition() - 1)
                self.caret.moveLeft()
            elif event.key == self.left:
                self.caret.moveLeft()
            elif event.key == self.right:
                self.caret.moveRight()













