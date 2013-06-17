import pygame
import ui.uievent
from ui import internals
from ui.uicomponent import *

class Button(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

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
    
    def mouseOneReleaseCollide(self, event):
        pygame.event.post(ui.uievent.ButtonPressEvent(self).getEvent())














