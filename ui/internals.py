import ui.eventdispatcher

#Listeners
mouseMoveListeners = ui.eventdispatcher.EventDispatcher()

mouseOnePressListeners = ui.eventdispatcher.EventDispatcher()

mouseOneReleaseListeners = ui.eventdispatcher.EventDispatcher()

#Event types: keys are event types, values are listeners for those event types
event_types={}

#CONSTANTS:
UIEVENT = 25

#Event IDs:
BUTTONPRESSEVENT = 25.0001
