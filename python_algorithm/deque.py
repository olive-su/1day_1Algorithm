from collections import deque

N = int(input())
my_deque = deque()
for _ in range(N):
    c = input().split()
    if c[0] == 'size':
        print(len(my_deque))
    elif c[0] == 'empty':
        if my_deque: print(0)
        else: print(1)
    elif c[0] == 'front':
        if my_deque: print(my_deque[0])
        else: print(-1)
    elif c[0] == 'back':
        if my_deque: print(my_deque[-1])
        else: print(-1)
    elif c[0] == 'push_front':
        my_deque.appendleft(c[1])
    elif c[0] == 'push_back':
        my_deque.append(c[1])
    elif c[0] == 'pop_front':
        if my_deque:print(my_deque.popleft())
        else: print(-1)
    else:
        if my_deque:print(my_deque.pop())
        else: print(-1)
