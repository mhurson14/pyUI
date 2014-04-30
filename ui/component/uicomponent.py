from framework.object.baseobject import BaseObject

import ui
import framework


class UIComponent(BaseObject):
    '''
    UIComponent is the base-class of all components.  It contains basic functionality
    useful to all components.
    '''
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):
        '''
        The constructor for UIComponent
        
        @param parent: The parent component which contains this component.  This
        should be an instance of UIComponent or any of its sub-classes.  All
        components should have a parent with the exception of L{ui.screen.Screen}.
        If you wish to draw a component directly to the screen, then its parent
        should be set to L{ui.screen.Screen}.  If a component is going to be added
        to a UIContainer using either L{ui.uicomponent.UIContainer.addComponent} or
        L{ui.uicomponent.UIContainer.addComponents}, then parent may be set to None,
        as either of those methods will set the parent attribute of the added
        components.
        @type parent: L{ui.uicomponent.UIComponent}
        
        @param surface: The type of display surface to use when displaying this
        component.  This should be L{ui.displaysurface.DisplaySurface} or one of
        its subclasses.
        @type surface: type

        @param graphics: The type of graphics object to control how the component
        displays.  This should be a subclass of L{ui.uigraphics.UIGraphics}.
        @type graphics: type

        @param surface_params: The parameters that will be used to instantiate the
        display surface for this component.  This should be a subclass of
        L{ui.parameters.Parameters}.
        @type surface_params: L{ui.parameters.Parameters}

        @param graphics_params: The parameters that will be used to instantiate the
        graphics object for this component. This should be a subclass of
        L{ui.parameters.Parameters}.
        @type graphics_params: L{ui.parameters.Parameters}

        @post: This component's display_surface attribute references an instance
        of type surface initialized with surface_params.
        @post: This component's graphics attribute references an instance of type
        graphics initialized with graphics_params.
        '''

        super().__init__(parent, surface, graphics, surface_params, graphics_params)
        
        self.state = 'normal'
        '''
        A string representing the state of this component with respect to the mouse.

        Possible states are:
            - normal: The default state.  This means that the mouse is not currently
            interacting with this component
            - hover: The mouse is currently hovering over this component.
            - pressed: The left mouse button has been pressed on this component.

        Note: The state will always be normal unless this component is listening to
        L{ui.internals.MOUSEMOTIONEVENT}, L{ui.internals.MOUSEBUTTONDOWNEVENT},
        or L{ui.internals.MOUSEBUTTONUPEVENT}

        See: L{setState}, L{onMouseMove}, L{onMouseOnePress}, L{onMouseOneRelease},
        L{mouseMoveCollide}, L{mouseMoveMiss}, L{pressedMouseMoveCollide},
        L{pressedMouseMoveMiss}, L{mouseOnePressCollide}, L{mouseOnePressMiss},
        L{mouseOneReleaseCollide}, L{mouseOneReleaseMiss},
        L{pressedMouseOneReleaseCollide}, L{pressedMouseOneReleaseMiss}
        '''

    def setState(self, state):
        '''
        setState sets the L{state} of this component.

        @param state: A string representing the state to set this component to.
        See L{state} for acceptable values.
        @type state: String

        @post: The state of this component has been set to state.

        See: L{state}
        '''
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
        else:
            if self.absolute_rect.collidepoint(event.pos):
                self.pressedMouseMoveCollide(event)
            else:
                self.pressedMouseMoveMiss(event)
    
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

class FocusableUIComponent(UIComponent):
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):
        
        super().__init__(parent, surface, graphics,
                         surface_params, graphics_params)
        
        self.focus = False

        self.registerEvent(framework.internals.MOUSEBUTTONDOWNEVENT, self.onMouseOnePress)
        self.registerEvent(framework.internals.MOUSEBUTTONUPEVENT, self.onMouseOneRelease)

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














