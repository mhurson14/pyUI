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

        self.registerEvent(internals.MOUSEMOTIONEVENT, self.onMouseMove)
        self.registerEvent(internals.MOUSEBUTTONDOWNEVENT, self.onMouseOnePress)
        self.registerEvent(internals.MOUSEBUTTONUPEVENT, self.onMouseOneRelease)

    def drawMembers(self):
        self.text.draw()

    def setMembersVisible(self, val):
        self.text.setVisibleRecursive(val)

    def setState(self, state):
        self.graphics.setState(state)
        self.state = state
    
    def pressedMouseOneReleaseCollide(self, event):
        pygame.event.post(ui.uievent.ButtonPressEvent(self).getEvent())














