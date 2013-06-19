import ui
from ui import internals
from ui.eventdispatcher import EventDispatcher

def init():
    print("Initializing...")
    ui.event.createDispatcher(internals.MOUSEMOTIONEVENT)
    ui.event.createDispatcher(internals.MOUSEBUTTONDOWNEVENT)
    ui.event.createDispatcher(internals.MOUSEBUTTONUPEVENT)
    ui.event.createDispatcher(internals.BUTTONPRESSEVENT)
    ui.event.createDispatcher(internals.KEYDOWNEVENT)
    ui.event.createDispatcher(internals.CARETTIMEREVENT)
    print("Done!")
