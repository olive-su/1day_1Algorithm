from sys import stdin
from collections import deque


n, m, t = map(int, stdin.readline().split())
maps = []
for _ in range(n):
    li = list(map(int, stdin.readline().split()))
    maps.append(li)

maps[0][0] = -1
global rst
rst = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    global rst
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] - 1
                queue.append((nx, ny))
            elif maps[nx][ny] == 2:
                rst = -maps[x][y] + ((m-1) - ny) + ((n-1) - nx)
                maps[nx][ny] = maps[x][y] - 1
                queue.append((nx, ny))


bfs(0, 0)

if maps[n-1][m-1] != 0:
    maps[n-1][m-1] = -maps[n-1][m-1] - 1
    if rst != 0:
        rst = min(rst, maps[n-1][m-1])
    else:
        rst = maps[n-1][m-1]

if rst != 0 and rst <= t:
    print(rst)
else:
    print('Fail')

