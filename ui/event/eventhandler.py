import ui
from ui.event.eventtimerhandler import *
from ui.event import eventdispatcher


class EventHandler:
    def __init__(self):
        #Event types:
        #    key: the event type
        #    val: the dispatcher for the event type
        self.event_types={}

        self.timer_handler = EventTimerHandler()

    def start(self):
        self.timer_handler.start()

    def stop(self):
        self.timer_handler.stop()
    
    def process(self, event):
        #print(UIEVENT)
        if event.type == ui.internals.UIEVENT and event.ui_type in self.event_types:
            self.event_types[event.ui_type].notify(event)
        elif event.type in self.event_types:
            self.event_types[event.type].notify(event)

    def createDispatcher(self, event_type):
        if event_type not in self.event_types:
            self.event_types[event_type] = eventdispatcher.EventDispatcher()

    def addListener(self, event_type, listener, method):
        self.event_types[event_type].addListener(listener, method)

    def removeListener(self, event_type, listener):
        self.event_types[event_type].removeListener(listener)

    def addTimer(self, timer):
        self.timer_handler.addTimer(timer)

    def removeTimer(self, timer):
        self.timer_handler.removeTimer(timer)

    def setTimerUpdateRate(self, rate):
        self.timer_handler.setFrameRate(rate)

    def sleepTimers(self, time_in):
        self.timer_handler.setSleepTime(time_in)








