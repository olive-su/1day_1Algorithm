import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)] 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((a, b))
    graph[b].append((b, a))

def bfs():
    queue = deque([])
    visited[1] = 0
    for i, j in graph[1]:
        queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        if visited[y] == -1:
            visited[y] = visited[x] + 1
            for i, j in graph[y]:
                queue.append((i, j))

rst1, rst2, rst3 = 0, 0, 0
bfs()
for i in range(n + 1):
    if visited[i] > rst2:
        rst1 = i
        rst2 = visited[i]
        rst3 = 1
    elif visited[i] == rst2:
        rst3 += 1
print(rst1, rst2, rst3)
