# boj. 1260

import sys
from collections import deque
from heapq import *

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer_dfs = []
answer_bfs = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i = i.sort()

def dfs(num):
    visited[num] = True
    answer_dfs.append(str(num))
    for i in graph[num]:
        if not visited[i]:
            dfs(i)

dfs(v)

visited = [False] * (n + 1)

def bfs(num):
    queue = deque([num])
    visited[num] = True
    
    while queue:
        a = queue.popleft()
        answer_bfs.append(str(a))
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(v)

print(' '.join(answer_dfs))
print(' '.join(answer_bfs))

