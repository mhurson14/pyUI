import pygame
import threading, time
from ui.eventtimercontainer import EventTimerContainer

class EventTimerHandler:
    def __init__(self):

        self.timers = EventTimerContainer()

        self.running = True

        self.thread = threading.Thread(None, self.run)
        self.thread.daemon = True

        self.clock = pygame.time.Clock()

        self.frame_rate = 60

        self.sleep_time = 0

        self.lock = threading.Lock()

    def setSleepTime(self, time):
        self.lock.acquire()
        self.sleep_time = time
        self.lock.release()

    def setFrameRate(self, rate):
        self.frame_rate = rate

    def start(self):
        self.thread.start()
        #self.thread.run()

    def stop(self):
        self.running = False
        self.thread.join()

    def setRunning(self, val):
        self.running = val

    def run(self):
        while self.running:
            self.clock.tick(self.frame_rate)
            self.timers.processTimers()

            if self.sleep_time != 0:
                time.sleep(self.sleep_time)
                self.setSleepTime(0)

    def addTimer(self, timer):
        self.timers.addTimer(timer)

    def removeTimer(self, timer):
        self.timers.removeTimer(timer)
