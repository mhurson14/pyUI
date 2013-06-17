import pygame

class UIComponent:
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):

        self.parent = parent

        self.display_surface = surface(surface_params)

        self.graphics = graphics(graphics_params)

        self.visible = False

        self.absolute_rect = None

        self.calculateAbsoluteRect()

    

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














