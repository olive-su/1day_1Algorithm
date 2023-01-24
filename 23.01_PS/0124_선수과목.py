# boj. 14567
# time : 7'

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph, indegree, answer = [[] for _ in range (n + 1)], [0] * (n + 1), [1] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque([])
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    t = queue.popleft()
    for i in graph[t]:
        indegree[i] -= 1
        if not indegree[i]:
            answer[i] = answer[t] + 1
            queue.append(i)

[print(answer[i], end=' ') for i in range(1, n + 1)]