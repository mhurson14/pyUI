import pygame
import ui.uievent
from ui import internals
from ui.uicomponent import *

class Button(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.state = 'normal'

        self.text = text
        self.addMember(self.text)

    def drawMembers(self):
        self.text.draw()

    def setState(self, state):
        self.graphics.setState(state)
        self.state = state

    def setVisible(self, val):
        self.visible = val

        if val:
            #Add this button as a listener for mouse movements
            internals.mouseMoveListeners.addListener(self, self.onMouseMove)

            #Add this button as a listener for mouse press events
            internals.mouseOnePressListeners.addListener(self, self.onMouseOnePress)

            #Add this button as a listener for mouse release events
            internals.mouseOneReleaseListeners.addListener(self, self.onMouseOneRelease)
        else:
            #Add this button as a listener for mouse movements
            internals.mouseMoveListeners.removeListener(self)

            #Add this button as a listener for mouse press events
            internals.mouseOnePressListeners.removeListener(self)

            #Add this button as a listener for mouse release events
            internals.mouseOneReleaseListeners.removeListener(self)

    def onMouseMove(self, event):
        changed = False
        if self.state != 'pressed':
            if self.absolute_rect.collidepoint(event.pos):
                if self.state != 'hover':
                    changed = True
                self.setState('hover')
            elif self.state == 'hover':
                self.setState('normal')
                changed = True
            if changed:
                self.draw()

    def onMouseOnePress(self, event):
        if self.absolute_rect.collidepoint(event.pos):
            self.setState('pressed')
            self.draw()

    def onMouseOneRelease(self, event):
        if self.state == 'pressed':
            if self.absolute_rect.collidepoint(event.pos):
                self.setState('hover')
                pygame.event.post(ui.uievent.ButtonPressEvent(self).getEvent())
            else:
                self.setState('normal')
            self.draw()














