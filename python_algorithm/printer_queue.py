from collections import deque
from sys import stdin

def priority_queue():
    N, M = map(int, stdin.readline().split())
    printer = deque(map(int, stdin.readline().split()))
    for idx, i in enumerate(printer):
        printer[idx] = (idx, i)
    priority = 0
    while 1:
        if printer[0][1] == max(printer, key=lambda x: x[1])[1]:
            priority += 1
            if printer[0][0] == M:
                break
            printer.popleft() 
        else:
            printer.append(printer.popleft() )
    print(priority)

for _ in range(int(stdin.readline())):
    priority_queue()
