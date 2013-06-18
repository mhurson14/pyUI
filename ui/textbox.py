from ui.uicomponent import *
from ui import internals
import ui.caret
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
            self.caret = ui.caret.Caret(

        self.setValidKeys()

        self.registerEvent(internals.KEYDOWNEVENT, self.onKeyPress)

    def moveLeft(self):
        if self.caret_pos > 0:
            text = self.text.getText()
            newText = text[:self.caret_pos] + text[self.caret_pos + 1:]
            self.caret_pos -= 1
            newText = newText[:self.caret_pos] + self.caret_on +\
                      newText[self.caret_pos:]
            self.text.setText(newText)

    def moveRight(self):
        text = self.text.getText()
        if self.caret_pos < len(text) - 1:
            newText = text[:self.caret_pos] + text[self.caret_pos + 1:]
            self.caret_pos += 1
            newText = newText[:self.caret_pos] + self.caret_on +\
                      newText[self.caret_pos:]
            self.text.setText(newText)

    def setFocus(self, val):
        super().setFocus(val)
        if val:
            self.addToDispatcher(internals.KEYDOWNEVENT)
        else:
            self.removeFromDispatcher(internals.KEYDOWNEVENT)

    def setValidKeys(self):
        for i in range(32, 127):
            self.valid_keys[chr(i)] = i

    def drawMembers(self):
        self.text.draw()

    def onKeyPress(self, event):
        if self.hasFocus():
            if event.unicode in self.valid_keys:
                self.text.setText(self.text.getText() +
                                  event.unicode)
            elif event.key == self.backspace:
                self.text.setText(self.text.getText()[:-1])
            elif event.key == self.left:
                self.moveLeft()
            elif event.key == self.right:
                self.moveRight()













