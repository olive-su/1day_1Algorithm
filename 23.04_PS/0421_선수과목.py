# boj. 14567
# time: 20' 

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
answer = [[] for _ in range(n + 1)]
cnt = 1 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque([])
for i in range(1, n + 1):
    if not indegree[i]: 
        answer[i] = cnt
        q.append(i)

while q:
    x = q.popleft()
    for i in graph[x]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)
            answer[i] = answer[x] + 1
        

[print(answer[i], end = ' ') for i in range(1, n + 1)]
