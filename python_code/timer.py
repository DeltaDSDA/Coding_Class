import time
import datetime
import os

class Timer:

    def __init__(self):
        self._hour = 0
        self._minute = 0
        self._second = 0
        self._hundi_second = 0

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        default = time.time()
        while True:
            ts = time.time() - default + 3600*15
            st = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S.%f")
            st = st[:-4]
            self.cls()
            print(st)

if __name__ == "__main__":
    new = Timer()
    new.run()
