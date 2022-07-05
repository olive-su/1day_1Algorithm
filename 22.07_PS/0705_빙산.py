# boj. 2573

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
time = 1
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def melt(x, y, new):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not graph[ny][nx]:
            cnt += 1
    new[y][x] = max(0, graph[y][x] - cnt) # 음수방지

def bfs(x, y, visited):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and graph[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
    return visited

while True:
    stop = 1
    cnt = 0
    visited = [([0] * m) for _ in range(n)]
    new = [([0] * m) for _ in range(n)]

    # 섬 녹음
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                stop = 0
                melt(j, i, new)

    if stop:
        sys.exit(print(0))

    graph = new

    # 분리된 섬 개수 파악
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                if cnt:
                    sys.exit(print(time))
                visited = bfs(j, i, visited)
                cnt = 1

    time += 1
