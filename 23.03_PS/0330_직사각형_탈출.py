# boj. 16973
# time: 30'

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
graph = []
for _ in range(n):
    graph.append(list(input().split()))
h, w, sr, sc, fr, fc = map(int, input().split())
visited = [[-1 for _ in range(m)] for _ in range(n)]

def is_square(y, x):
    for i in range(y, y + h):
        for j in range(x, x + w):
            if n <= i or m <= j or graph[i][j] != '0':
                return False
    return True

visited[sr - 1][sc - 1] = 0
queue = deque([(sr - 1, sc - 1)])

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
            if is_square(ny, nx):
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
            else:
                visited[ny][nx] = -2

if visited[fr - 1][fc - 1] < 0:
    print(-1)
else:
    print(visited[fr - 1][fc - 1])