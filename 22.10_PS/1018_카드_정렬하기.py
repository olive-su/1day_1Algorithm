# boj. 1715

import sys
from heapq import *

input = sys.stdin.readline

answer = 0;
n = int(input())
priority_queue = []
for _ in range(n):
    heappush(priority_queue, int(input()))

while len(priority_queue) > 1:
    t = heappop(priority_queue) + heappop(priority_queue)
    heappush(priority_queue, t)
    answer += t

print(answer)
