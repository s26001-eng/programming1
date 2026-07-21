queue = []
queue.append(1)
print('queue:', queue)
queue.append(2)
print('queue:', queue)
print('pop from queue 1st value:', queue.pop(0))
print('pop from queue 2nd value:', queue.pop(0))
print('queue:', queue)

from collections import deque
queue = deque([1, 2])
queue.append(3)
queue.append(4)
print('queue:', queue)
print('popleft from queue 1st value:', queue.popleft())
print('popleft from queue 2nd value:', queue.popleft())
print('queue:', queue)
