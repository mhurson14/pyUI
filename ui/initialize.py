from ui import internals
from ui import event
from ui.eventdispatcher import EventDispatcher

def init():
    print("Initializing...")
    event.registerEventAndDispatcher(internals.BUTTONPRESSEVENT, EventDispatcher())
    print("Done!")
