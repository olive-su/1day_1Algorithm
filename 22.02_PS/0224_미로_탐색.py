from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
maps = []
visited = []

for _ in range(n):
    maps.append(list(map(int, list(stdin.readline().rstrip()))))
    visited.append([False] * m)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True  # 방문처리
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문처리
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))


bfs(0, 0)
print(maps[n - 1][m - 1])

