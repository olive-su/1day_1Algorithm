# boj. 1766
# time : 12'

import sys
from heapq import *

input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

pq = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heappush(pq, i)

while pq:
    t = heappop(pq)
    print(t, end = ' ')
    for i in graph[t]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(pq, i)
