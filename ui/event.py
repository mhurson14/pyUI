import pygame
from pygame.locals import *
from ui.internals import *

def process(event):
    if event.type == MOUSEMOTION:
        mouseMoveListeners.notify(event)
    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        mouseOnePressListeners.notify(event)
    elif event.type == MOUSEBUTTONUP and event.button == 1:
        mouseOneReleaseListeners.notify(event)
    elif event.type == UIEVENT and event.ui_type in event_types:
        event_types[event.ui_type].notify(event)

def registerEventAndDispatcher(event_type, dispatcher):
    event_types[event_type] = dispatcher

def addListener(event_type, listener, method):
    event_types[event_type].addListener(listener, method)
