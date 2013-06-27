import pygame.event
import ui

class UIEvent():
    def __init__(self, typeIn, **kwargs):
        kwargs['ui_type'] = typeIn
        #self.pygame_event = pygame.event.Event(int(typeIn), **kwargs)
        self.pygame_event = pygame.event.Event(ui.internals.UIEVENT, **kwargs)

    def getEvent(self):
        return self.pygame_event

class ButtonPressEvent(UIEvent):
    def __init__(self, button):
        super().__init__(ui.internals.BUTTONPRESSEVENT, button=button)

class CaretBlinkEvent(UIEvent):
    def __init__(self, caret):
        super().__init__(ui.internals.CARETTIMEREVENT, caret=caret)


