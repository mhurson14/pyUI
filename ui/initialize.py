from ui import internals
from ui import event
from ui.eventdispatcher import EventDispatcher

def init():
    print("Initializing...")
    event.createDispatcher(internals.MOUSEMOTIONEVENT)
    event.createDispatcher(internals.MOUSEBUTTONDOWNEVENT)
    event.createDispatcher(internals.MOUSEBUTTONUPEVENT)
    event.createDispatcher(internals.BUTTONPRESSEVENT)
    event.createDispatcher(internals.KEYDOWNEVENT)
    print("Done!")
