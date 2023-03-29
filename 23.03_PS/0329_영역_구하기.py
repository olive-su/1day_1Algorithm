# boj. 2583
# time: 27'

import sys
from collections import deque

input = sys.stdin.readline
m, n, k = map(int, input().split())
graph = [[False for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = True

def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    rst = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and not graph[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
                rst += 1
    return rst

for i in range(m):
    for j in range(n):
        if not visited[i][j] and not graph[i][j]:
            answer.append(bfs(i, j))

print(len(answer))
[print(i, end=' ') for i in sorted(answer)]


