import queue

s = queue.Queue()


for i in range(6):
    s.push(i)
s.pop()
print(s.storage)
print(s.top)
print(s.bottom)

