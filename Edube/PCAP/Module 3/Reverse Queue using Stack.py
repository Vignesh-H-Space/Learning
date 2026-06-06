from collections import deque

queue = deque([10, 20, 30, 40])
stack = []

while queue:
    stack.append(queue.popleft())

while stack:
    queue.append(stack.pop())
