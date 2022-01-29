from sys import stdin
from collections import deque

t = int(stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    queue = deque()
    graph[y][x] = 0
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx]:
                graph[ny][nx] = 0
                queue.append((nx, ny))


for _ in range(t):
    rst = 0
    m, n, k = map(int, stdin.readline().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                rst += 1
                bfs(arr, j, i)
    print(rst)
