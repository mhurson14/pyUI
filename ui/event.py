import pygame
from pygame.locals import *
from ui.internals import *
from ui import eventdispatcher

def process(event):
    if event.type == UIEVENT and event.ui_type in event_types:
        event_types[event.ui_type].notify(event)
    elif event.type in event_types:
        event_types[event.type].notify(event)

def createDispatcher(event_type):
    if event_type not in event_types:
        event_types[event_type] = eventdispatcher.EventDispatcher()

def addListener(event_type, listener, method):
    event_types[event_type].addListener(listener, method)

def removeListener(event_type, listener):
    event_types[event_type].removeListener(listener)
