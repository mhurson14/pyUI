import pygame
import time
import threading
from framework.exceptions import initializationerror


class EventTimer:
    def __init__(self, event, time_ms):
        self.event = event

        self.time = time_ms

        self.last_trigger = None

        self.lock = threading.Lock()

    def start(self):
        self.lock.acquire()
        self.last_trigger = time.time()
        pygame.event.post(self.event)
        self.lock.release()

    def update(self):
        self.lock.acquire()
        if self.last_trigger:
            now = time.time()
            change = now - self.last_trigger
            change *= 1000

            num = int(change // self.time)
            self.last_trigger += num * self.time / 1000
            '''if num > 0:
                self.last_trigger = now'''

            for i in range(num):
                pygame.event.post(self.event)
        else:
            self.lock.release()
            raise initializationerror.InitializationError("Timer not initialized")
        self.lock.release()
