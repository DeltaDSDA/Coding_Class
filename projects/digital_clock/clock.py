import datetime
import pygame as pg
import winsound as ws
import threading

class clock:
    def __init__(self):
        now = datetime.datetime.now()
        self.year  = now.year
        self.month = now.month
        self.day = now.day
        self.hour = now.hour
        self.minute = now.minute
        self.sec = now.second

    def Alarm(self, hour, minute, sec):

    def stopwatch(self):

    def update(self):
