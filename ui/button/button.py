import pygame
import framework
from ui.event import uievent
from ui.component.uicomponent import UIComponent

class Button(UIComponent):
    def __init__(self, parent, surface, graphics,
                 surface_params, graphics_params, text):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.text = text
        self.addMember(self.text)

        self.registerEvent(framework.internals.MOUSEMOTIONEVENT, self.onMouseMove)
        self.registerEvent(framework.internals.MOUSEBUTTONDOWNEVENT, self.onMouseOnePress)
        self.registerEvent(framework.internals.MOUSEBUTTONUPEVENT, self.onMouseOneRelease)

    def drawMembers(self):
        self.text.draw()

    def setMembersVisible(self, val):
        self.text.setVisibleRecursive(val)

    def setState(self, state):
        self.graphics.setState(state)
        self.state = state
    
    def pressedMouseOneReleaseCollide(self, event):
        pygame.event.post(uievent.ButtonPressEvent(self).getEvent())














