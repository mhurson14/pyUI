import pygame

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
        if self.absolute_rect.collidepoint(event.pos):
            self.setState('pressed')
            self.mouseOnePressCollide(event)
            self.draw()
    
    def onMouseOneRelease(self, event):
        if self.state == 'pressed':
            if self.absolute_rect.collidepoint(event.pos):
                self.setState('hover')
                self.mouseOneReleaseCollide(event)
            else:
                self.setState('normal')
                self.mouseOneReleaseMiss(event)
            self.draw()
    
    def mouseMoveCollide(self, event):
        pass
    
    def mouseMoveMiss(self, event):
        pass
    
    def mouseOnePressCollide(self, event):
        pass
    
    def mouseOneReleaseCollide(self, event):
        pass
    
    def mouseOneReleaseMiss(self, event):
        pass

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

    def setVisible(self, val):
        self.visible = val

    def getVisible(self):
        return self.visible

    def getDisplaySurface(self):
        return self.display_surface

    def setParent(self, parent):
        self.parent = parent
        self.calculateAbsoluteRect()

    def draw(self, parent_surface=None):
        if self.visible:
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

    def mouseOneReleaseCollide(self, event):
        self.focus = True

    def mouseOneReleaseMiss(self, event):
        self.focus = False
    
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

    def setVisible(self, val):
        self.visible = val

        for component in self.components:
            component.setVisible(val)

    def draw(self, parent_surface=None):
        if self.visible:
            self.display_surface.clear()
            self.graphics.draw(self.display_surface)

            for component in self.components:
                    component.draw()

            self.drawMembers()

            if parent_surface:
                parent_surface.displaySurface(self.display_surface)
            else:
                self.parent.getDisplaySurface().displaySurface(self.display_surface)














