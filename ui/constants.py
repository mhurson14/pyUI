import ui.eventdispatcher

class Internals:
    def __init__(self):
        #CONSTANTS:
        self.UIEVENT = 25

        #Event IDs:
        self.KEYDOWNEVENT = 2
        self.MOUSEMOTIONEVENT = 4
        self.MOUSEBUTTONDOWNEVENT = 5
        self.MOUSEBUTTONUPEVENT = 6
        self._BUTTONPRESSEVENT = .0001
        self._CARETTIMEREVENT = .0002

    def setUIEvent(self, val):
        self.UIEVENT = val

    @property
    def BUTTONPRESSEVENT(self):
        return self._BUTTONPRESSEVENT + self.UIEVENT

    @BUTTONPRESSEVENT.setter
    def BUTTONPRESSEVENT(self, val):
        self._BUTTONPRESSEVENT = val

    @property
    def CARETTIMEREVENT(self):
        return self._CARETTIMEREVENT + self.UIEVENT

    @CARETTIMEREVENT.setter
    def CARETTIMEREVENT(self, val):
        self._CARETTIMEREVENT = val

    
