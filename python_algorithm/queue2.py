from collections import deque
import sys

queue = deque()
x = int(sys.stdin.readline().rstrip())
for _ in range(x):
    y = sys.stdin.readline().rstrip()
    if y == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif y == 'size':
        print(len(queue))
    elif y == 'empty':
        if queue: print(0)
        else: print(1)
    elif y == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif y == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    else:
        queue.append(int(y[5:]))
