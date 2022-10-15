# boj. 2178

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
count = 0

for _ in range(n):
    a = list(map(int, list(input().rstrip())))
    graph.append(a)

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx]:
                if not visited[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1

bfs(0, 0)
print(visited[n - 1][m - 1])