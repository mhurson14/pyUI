import ui


def init(ui_event_id=25):
    print("Initializing...")
    ui.internals.setUIEvent(ui_event_id)
    ui.event.createDispatcher(ui.internals.MOUSEMOTIONEVENT)
    ui.event.createDispatcher(ui.internals.MOUSEBUTTONDOWNEVENT)
    ui.event.createDispatcher(ui.internals.MOUSEBUTTONUPEVENT)
    ui.event.createDispatcher(ui.internals.BUTTONPRESSEVENT)
    ui.event.createDispatcher(ui.internals.KEYDOWNEVENT)
    ui.event.createDispatcher(ui.internals.CARETTIMEREVENT)
    print("Done!")
