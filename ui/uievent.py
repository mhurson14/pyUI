import pygame.event
import ui.internals

class UIEvent():
    def __init__(self, typeIn, **kwargs):
        kwargs['ui_type'] = typeIn
        self.pygame_event = pygame.event.Event(int(typeIn), **kwargs)

    def getEvent(self):
        return self.pygame_event

class ButtonPressEvent(UIEvent):
    def __init__(self, button):
        super().__init__(ui.internals.BUTTONPRESSEVENT, button=button)


