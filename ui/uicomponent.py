import pygame
import ui
from ui import internals

class UIComponent:
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):

        self.parent = parent

        self.display_surface = surface(surface_params)

        self.graphics = graphics(graphics_params)

        self.surface_type = surface
        self.graphics_type = graphics
        self.surface_params = surface_params
        self.graphics_params = graphics_params

        self.visible = False

        self.absolute_rect = None

        self.calculateAbsoluteRect()
        
        self.state = 'normal'

        #A dictionary containing the events this component is following:
        #   key: the ui_type of the event
        #   val: the function to be called in response to the event
        self.events = {}

        self.timers = {}

    def setState(self, state):
        self.state = state

    def onMouseMove(self, event):
        changed = False
        if self.state != 'pressed':
            if self.absolute_rect.collidepoint(event.pos):
                if self.state != 'hover':
                    changed = True
                self.setState('hover')
                self.mouseMoveCollide(event)
            elif self.state == 'hover':
                self.setState('normal')
                changed = True
                self.mouseMoveMiss(event)
            if changed:
                self.draw()
    
    def onMouseOnePress(self, event):
        if event.button == 1 and self.absolute_rect.collidepoint(event.pos):
            self.setState('pressed')
            self.mouseOnePressCollide(event)
            self.draw()
        elif event.button == 1:
            self.mouseOnePressMiss(event)
    
    def onMouseOneRelease(self, event):
        if event.button == 1:
            if self.state == 'pressed':
                if self.absolute_rect.collidepoint(event.pos):
                    self.setState('hover')
                    self.pressedMouseOneReleaseCollide(event)
                else:
                    self.setState('normal')
                    self.pressedMouseOneReleaseMiss(event)
                self.draw()
            else:
                if self.absolute_rect.collidepoint(event.pos):
                    self.mouseOneReleaseCollide(event)
                else:
                    self.mouseOneReleaseMiss(event)
    
    def mouseMoveCollide(self, event):
        pass
    
    def mouseMoveMiss(self, event):
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

    def registerTimer(self, timer):
        self.timers[timer] = True
        if self.getVisible():
            self.addTimer(timer)

    def addTimer(self, timer):
        timer.start()
        ui.event.addTimer(timer)

    def addTimers(self):
        for timer in self.timers:
            self.addTimer(timer)

    def removeTimer(self, timer):
        ui.event.removeTimer(timer)

    def removeTimers(self):
        for timer in self.timers:
            self.removeTimer(timer)

    def registerEvent(self, event_type, method):
        self.events[event_type] = method
        if self.getVisible():
            self.addToDispatcher(event_type)

    def addToDispatcher(self, event):
        ui.event.addListener(event, self, self.events[event])

    def addToDispatchers(self):
        for event in self.events:
            ui.event.addListener(event, self, self.events[event])

    def removeFromDispatcher(self, event):
        ui.event.removeListener(event, self)

    def removeFromDispatchers(self):
        for event in self.events:
            ui.event.removeListener(event, self)
    
    def addMember(self, member):
        member.setParent(self)

    def calculateAbsoluteRect(self):
        if self.parent:
            parent_rect = self.parent.getAbsoluteRect()
            if parent_rect:
                self.absolute_rect = pygame.Rect(self.display_surface.getRect())
                self.absolute_rect.left += parent_rect.left
                self.absolute_rect.top += parent_rect.top

    def getAbsoluteRect(self):
        if self.absolute_rect:
            return self.absolute_rect
        else:
            self.calculateAbsoluteRect()
            return self.absolute_rect

    def getRelativeRect(self):
        return self.display_surface.getRect()

    def setVisible(self, val):
        self.visible = val
        if self.visible:
            self.addToDispatchers()
            self.addTimers()
        else:
            self.removeFromDispatchers()
            self.removeTimers()

    def setVisibleRecursive(self, val):
        self.setVisible(val)

        self.setMembersVisible(val)

    def setMembersVisible(self, val):
        pass

    def getVisible(self):
        return self.visible

    def getDisplaySurface(self):
        return self.display_surface

    def setParent(self, parent):
        self.parent = parent
        self.calculateAbsoluteRect()

    def draw(self, parent_surface=None):
        if self.getVisible():
            self.display_surface.clear()
            self.graphics.draw(self.display_surface)

            self.drawMembers()

            if parent_surface:
                parent_surface.displaySurface(self.display_surface)
            else:
                self.parent.getDisplaySurface().displaySurface(self.display_surface)

    def drawMembers(self):
        pass

class FocusableUIComponent(UIComponent):
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):
        
        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.focus = False

        self.registerEvent(internals.MOUSEBUTTONDOWNEVENT, self.onMouseOnePress)
        self.registerEvent(internals.MOUSEBUTTONUPEVENT, self.onMouseOneRelease)

    def mouseOnePressCollide(self, event):
        self.setFocus(True)

    def mouseOnePressMiss(self, event):
        self.setFocus(False)
    
    def hasFocus(self):
        return self.focus
    
    def setFocus(self, val):
        self.focus = val

class UIContainer(UIComponent):
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):

        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)

        self.components = []

    def addComponent(self, component):
        component.setParent(self)
        self.components.append(component)

    def addComponents(self, components):
        for component in components:
            component.setParent(self)
            self.components.append(component)

    def setVisibleRecursive(self, val):
        self.setVisible(val)

        for component in self.components:
            component.setVisibleRecursive(val)

        self.setMembersVisible(val)

    def draw(self, parent_surface=None):
        if self.getVisible():
            self.display_surface.clear()
            self.graphics.draw(self.display_surface)

            for component in self.components:
                    component.draw()

            self.drawMembers()

            if parent_surface:
                parent_surface.displaySurface(self.display_surface)
            else:
                self.parent.getDisplaySurface().displaySurface(self.display_surface)














