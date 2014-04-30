__author__ = 'mhurson'

import pygame
import framework


class BaseObject:
    '''
    BaseObject is the base-class of all displayable objects
    '''
    def __init__(self, parent, surface, graphics, surface_params, graphics_params):
        '''
        The constructor for BaseObject

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

    def registerTimer(self, timer):
        self.timers[timer] = True
        if self.getVisible():
            self.addTimer(timer)

    def addTimer(self, timer):
        timer.start()
        framework.eventHandler.addTimer(timer)

    def addTimers(self):
        for timer in self.timers:
            self.addTimer(timer)

    def removeTimer(self, timer):
        framework.eventHandler.removeTimer(timer)

    def removeTimers(self):
        for timer in self.timers:
            self.removeTimer(timer)

    def registerEvent(self, event_type, method):
        self.events[event_type] = method
        if self.getVisible():
            self.addToDispatcher(event_type)

    def addToDispatcher(self, event):
        framework.eventHandler.addListener(event, self, self.events[event])

    def addToDispatchers(self):
        for event in self.events:
            framework.eventHandler.addListener(event, self, self.events[event])

    def removeFromDispatcher(self, event):
        framework.eventHandler.removeListener(event, self)

    def removeFromDispatchers(self):
        for event in self.events:
            framework.eventHandler.removeListener(event, self)

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