import threading

class EventTimerContainer:
    def __init__(self):
        self.timers = {}
        self.lock = threading.Lock()

    def addTimer(self, timer):
        self.lock.acquire()
        if timer not in self.timers:
            self.timers[timer] = True
        self.lock.release()

    def removeTimer(self, timer):
        self.lock.acquire()
        if timer in self.timers:
            del self.timers[timer]
            self.lock.release()
            return True
        else:
            self.lock.release()
            return False

    def contains(self, timer):
        return timer in self.timers

    def processTimers(self):
        self.lock.acquire()
        for timer in self.timers:
            timer.update()
        self.lock.release()
