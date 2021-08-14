from collections import deque
from multiprocessing import Queue
from queue import PriorityQueue

print('\n using deque')
queue = deque()
queue.append('hi')
queue.append('hey')
queue.append('hello')
print(queue)
print()

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print('\n using Queue')
q = Queue()
q.put('hi')
q.put('hey')
q.put('hello')
print(q)
print(q.get())
print(q.get())
print(q.get())

print('\n using Priority Queue')
q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)
