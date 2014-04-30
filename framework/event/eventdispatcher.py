

class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def addListener(self, listener, method):
        self.listeners[listener] = method

    def removeListener(self, listener):
        try:
            del self.listeners[listener]
            return True
        except KeyError as e:
            return False

    def notify(self, event):
        for listener in self.listeners:
            if listener.getVisible():
                method = self.listeners[listener]
                method(event)
