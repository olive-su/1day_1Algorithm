import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph, visited = [], []
for _ in range(m):
    graph.append(list(map(int, input().split())))
    visited.append([0] * n)
rst = 0

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def bfs(y, x):
    visited[y][x] = 1
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            rst += 1

print(rst)