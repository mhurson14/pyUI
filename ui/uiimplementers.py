import pygame
from pygame.locals import *

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
        self.setSelected()

    def pressedMouseMoveMiss(self, event):
        start_x = self.text.getAbsoluteHorizontalCoordinate(self.start)
        if event.pos[0] <= start_x:
            self.end = 0
        else:
            self.end = self.text.getEnd()
        self.setSelected()
    
    def mouseOnePressCollide(self, event):
        keys = pygame.key.get_pressed()
        if keys[K_RSHIFT] or keys[K_LSHIFT]:
            pass
        else:
            position = self.text.getClickedPosition(event.pos)
            if position != None:
                self.start = position
                self.end = position
            else:
                end = self.text.getEnd()
                self.start = end
                self.end = end
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
        else:
            self.start = self.caret.getPosition()
            self.end = self.caret.getPosition()
        self.setSelected()


    def onSetVisible(self, val):
        pass

    def onSetFocus(self, val):
        pass
