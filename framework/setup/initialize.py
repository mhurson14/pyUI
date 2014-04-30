import framework


def init(ui_event_id=25):
    print("Initializing...")
    framework.internals.setUIEvent(ui_event_id)
    framework.eventHandler.createDispatcher(framework.internals.MOUSEMOTIONEVENT)
    framework.eventHandler.createDispatcher(framework.internals.MOUSEBUTTONDOWNEVENT)
    framework.eventHandler.createDispatcher(framework.internals.MOUSEBUTTONUPEVENT)
    framework.eventHandler.createDispatcher(framework.internals.BUTTONPRESSEVENT)
    framework.eventHandler.createDispatcher(framework.internals.KEYDOWNEVENT)
    framework.eventHandler.createDispatcher(framework.internals.CARETTIMEREVENT)
    print("Done!")
