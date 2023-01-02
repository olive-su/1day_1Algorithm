# boj. 1261
# time : 30'

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
graph, visited = [], []
for _ in range(n):
    graph.append(list(input().rstrip()))
    visited.append([-1] * m)

visited[0][0] = 0
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    if x == m - 1 and y == n - 1: # 목적지 도착
        exit(print(visited[y][x]))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1: # 미방문
                if graph[ny][nx] == '0': # 빈 방
                    visited[ny][nx] = visited[y][x]
                    queue.appendleft((nx, ny))
                else: # 벽
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx, ny))
