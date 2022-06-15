import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(q) == 0:
            print(0)
        else:
            _, v = heappop(q)
            print(v)
    else:
        heappush(q, (abs(m), m))


