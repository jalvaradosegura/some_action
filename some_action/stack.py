# LIFO (Last In First Out)
from collections import deque
from queue import LifoQueue

print('using deque')
stack = deque()
stack.append('hi')
stack.append('hey')
stack.append('hello')
print(stack)
print()

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

print('\nusing LifoQueue')
stack = LifoQueue()
stack.put('hi')
stack.put('hey')
stack.put('hello')
print(stack)
print()

print(stack.get())
print(stack.get())
print(stack.get())
