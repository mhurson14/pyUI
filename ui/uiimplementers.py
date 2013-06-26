import pygame
from pygame.locals import *
import ui

class UIImplementer:
    def __init__(self):
        pass

    def mouseMoveCollide(self, event):
        pass
    
    def mouseMoveMiss(self, event):
        pass

    def pressedMouseMoveCollide(self, event):
        pass

    def pressedMouseMoveMiss(self, event):
        pass
    
    def mouseOnePressCollide(self, event):
        pass

    def mouseOnePressMiss(self, event):
        pass

    def mouseOneReleaseCollide(self, event):
        pass

    def mouseOneReleaseMiss(self, event):
        pass
    
    def pressedMouseOneReleaseCollide(self, event):
        pass
    
    def pressedMouseOneReleaseMiss(self, event):
        pass

    def onKeyPress(self, event):
        pass

    def onSetVisible(self, val):
        pass

    def onSetFocus(self, val):
        pass

class TextSelecter (UIImplementer):
    def __init__(self, text, caret):

        super().__init__()

        self.text = text
        self.caret = caret
        
        self.start = 0
        self.end = 0

        self.keys = {K_LEFT:True, K_RIGHT:True, K_HOME:True, K_END:True}

    def setSelected(self):
        if self.start > self.end:
            self.text.setSelected(self.end, self.start)
        else:
            self.text.setSelected(self.start, self.end)
    
    def pressedMouseMoveCollide(self, event):
        position = self.text.getClickedPosition(event.pos)
        if position != None:
            self.end = position
        else:
            start_x = self.text.getAbsoluteHorizontalCoordinate(self.start)
            if event.pos[0] <= start_x:
                self.end = 0
            else:
                self.end = self.text.getEnd()
        self.caret.setLocation(self.end)
        self.setSelected()

    def pressedMouseMoveMiss(self, event):
        start_x = self.text.getAbsoluteHorizontalCoordinate(self.start)
        if event.pos[0] <= start_x:
            self.end = 0
        else:
            self.end = self.text.getEnd()
        self.caret.setLocation(self.end)
        self.setSelected()
    
    def mouseOnePressCollide(self, event):
        keys = pygame.key.get_pressed()
        if keys[K_RSHIFT] or keys[K_LSHIFT]:
            self.end = self.caret.getPosition()
        else:
            self.start = self.caret.getPosition()
            self.end = self.caret.getPosition()
        self.setSelected()
    
    def pressedMouseOneReleaseCollide(self, event):
        position = self.text.getClickedPosition(event.pos)
        if position != None:
            self.end = position
        else:
            self.end = self.text.getEnd()
        self.setSelected()

    def onKeyPress(self, event):
        keys = pygame.key.get_pressed()
        if keys[K_RSHIFT] or keys[K_LSHIFT]:
            if event.key in self.keys:
                self.end = self.caret.getPosition()
            else:
                self.start = self.caret.getPosition()
                self.end = self.caret.getPosition()
        elif keys[K_RCTRL] or keys[K_LCTRL]:
            if event.key == K_a:
                self.start = 0
                self.end = self.caret.getPosition()
        else:
            self.start = self.caret.getPosition()
            self.end = self.caret.getPosition()
        self.setSelected()


    def onSetVisible(self, val):
        pass

    def onSetFocus(self, val):
        pass

class CaretHandler(UIImplementer):
    def __init__(self, text, caret, valid_keys):

        super().__init__()

        self.text = text

        self.caret = caret

        self.valid_keys = valid_keys

        self.left = K_LEFT
        self.right = K_RIGHT

        self.backspace = K_BACKSPACE
        self.delete = K_DELETE

        self.home = K_HOME
        self.end = K_END

    def mouseOnePressCollide(self, event):
        position = self.text.getClickedPosition(event.pos)
        if position == None:
            position = self.text.getEnd()
        self.caret.setLocation(position)

    def onKeyPress(self, event):
        if event.unicode in self.valid_keys:
            self.caret.moveRight()
        elif event.key == self.left:
            self.caret.moveLeft()
        elif event.key == self.right:
            self.caret.moveRight()
        elif event.key == self.home:
            self.caret.setLocation(0)
        elif event.key == self.end:
            self.caret.setLocation(len(self.text))

        if type(self.text) == ui.text.SelectableText:
            if event.key == self.backspace:
                if self.text.getSelectionStart() != self.text.getSelectionEnd():
                    self.caret.setLocation(self.text.getSelectionStart())
                else:
                    self.caret.setLocation(self.text.getSelectionStart() - 1)
            if event.key == self.delete:
                self.caret.setLocation(self.text.getSelectionStart())

        keys = pygame.key.get_pressed()
        if keys[K_RCTRL] or keys[K_LCTRL]:
            if event.key == K_a:
                self.caret.setLocation(self.text.getEnd())






































