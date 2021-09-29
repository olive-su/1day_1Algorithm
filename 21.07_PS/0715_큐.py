from collections import deque
import sys

queue = deque()
num = int(sys.stdin.readline())
for _ in range(num):
    command = sys.stdin.readline().split()
    if command[0] == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue: print(0)
        else: print(1)
    elif command[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif command[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    else:
        queue.append(int(command[1]))
