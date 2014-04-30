import pygame
from pygame.locals import *

import utils
from ui.component.uicomponent import *
from ui.caret import caret as c, caretgraphics
from ui.displaysurface import displaysurface
from ui import parameters


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
            self.caret = c.Caret(None, displaysurface.DisplaySurface,
                                 caretgraphics.DefaultCaretGraphics,
                                 parameters.DisplaySurfaceParameters(
                                     dimensions=(1, 20), topleft=tl,
                                     flags=SRCALPHA),
                                 ui.parameters.DefaultCaretGraphicsParameters(),
                                 self.text)
        self.addMember(self.caret)

        self.setValidKeys()

        self.caret_handler = ui.uiimplementers.CaretHandler(self.text, self.caret,
                                                            self.valid_keys)
        self.selecter = ui.uiimplementers.TextSelecter(self.text, self.caret)

        self.registerEvent(framework.internals.KEYDOWNEVENT, self.onKeyPress)
        self.registerEvent(framework.internals.MOUSEMOTIONEVENT, self.onMouseMove)

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
            self.addToDispatcher(framework.internals.KEYDOWNEVENT)
            self.caret.setVisibleRecursive(True)
        else:
            self.removeFromDispatcher(framework.internals.KEYDOWNEVENT)
            self.caret.setVisibleRecursive(False)

    def setValidKeys(self):
        for i in range(32, 127):
            self.valid_keys[chr(i)] = i

    def drawMembers(self):
        self.text.draw()
        self.caret.draw()

    def onKeyPress(self, event):
        if self.hasFocus():

            start = self.text.getSelectionStart()
            end = self.text.getSelectionEnd()
            keys = pygame.key.get_pressed()

            if event.unicode in self.valid_keys:
                if start != end:
                    self.text.deleteText(start, end - 1)
                self.text.insertText(event.unicode, start)
            elif event.key == self.backspace:
                if start == end:
                    self.text.deleteCharacter(self.caret.getPosition() - 1)
                else:
                    self.text.deleteText(start, end - 1)
            elif event.key == self.delete:
                if start == end:
                    self.text.deleteCharacter(self.caret.getPosition())
                else:
                    self.text.deleteText(start, end - 1)

            if keys[K_LCTRL] or keys[K_RCTRL]:
                if event.key == K_c and start != end:
                    utils.pyperclip.copy(self.text.getText()[start:end])
                elif event.key == K_v:
                    if start != end:
                        self.text.deleteText(start, end - 1)
                    self.text.insertText(utils.pyperclip.paste(), start)

            self.caret_handler.onKeyPress(event)
            self.selecter.onKeyPress(event)













