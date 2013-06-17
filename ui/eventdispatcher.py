

class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def addListener(self, listener, method):
        self.listeners[listener] = method

    def removeListener(self, listener):
        del self.listeners[listener]

    def notify(self, event):
        for listener in self.listeners:
            method = self.listeners[listener]
            method(event)
