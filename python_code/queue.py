class Queue(object):
    def __init__(self):
        self.storage = []
        self.top = 0
        self.bottom = 0

    def push(self, value):
        self.storage.insert(self.top, value)
        self.top = self.top+1

    def pop(self):
        value = self.storage.pop(self.bottom)
        self.top = self.top-1
        return value

    def isempty(self):
        if(self.top==self.bottom):
            return True
        else:
            return False
    
