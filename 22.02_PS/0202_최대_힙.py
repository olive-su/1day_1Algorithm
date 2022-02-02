from heapq import *
from sys import stdin
n = int(stdin.readline())
heap = []
for _ in range(n):
    command = int(stdin.readline())
    if command == 0:
        if len(heap) < 1:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-command, command))
