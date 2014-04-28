import pygame
import ui

class UIComponent:
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

        self.parent = parent
        '''The component that contains this component'''

        self.display_surface = surface(surface_params)
        '''The display surface on which this component will be rendered'''

        self.graphics = graphics(graphics_params)
        '''The graphics object that will control how this component is rendered'''

        self.surface_type = surface
        '''A reference to the display surface type that was passed to the constructor'''
        self.graphics_type = graphics
        '''A reference to the graphics type that was passed to the constructor'''
        self.surface_params = surface_params
        '''A reference to the surface parameters that were passed to the constructor'''
        self.graphics_params = graphics_params
        '''A reference to the graphics parameters that were passed to the constructor'''

        self.visible = False
        '''
        A boolean representing whether or not the component is currently visible.

        Values:
            - True if the component is currently visible
            - False otherwise.

        The visibility of a component controls whether the component is rendered,
        as well as whether it listens for events.
        '''

        self.absolute_rect = None
        '''
        A pygame rect with the dimensions of the component as well as the coordinates
        of the component relative to the topleft of the screen.
        '''

        self.calculateAbsoluteRect()
        
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
        
        self.events = {}
        '''
        A dictionary containing the event types that this component is currently
        listening to.

            - key: the ui_type of the event
            - val: the function to be called in response to the event

        See: L{registerEvent}, L{addToDispatcher}, L{addToDispatchers},
        L{removeFromDispatcher}, L{removeFromDispatchers}
        '''

        self.timers = {}
        '''
        A dictionary containing the event timers owned by this component.

            - key: the timer object
            - val: True

        The values for all keys are always True, and hold no particular meaning.

        See: L{registerTimer}, L{addTimer}, L{addTimers},
        L{removeTimer}, L{removeTimers}
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
        #if self.absolute_rect:
            # return self.absolute_rect
        # else:
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

        self.registerEvent(ui.internals.MOUSEBUTTONDOWNEVENT, self.onMouseOnePress)
        self.registerEvent(ui.internals.MOUSEBUTTONUPEVENT, self.onMouseOneRelease)

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














