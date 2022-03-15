from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())

maps, candy = [], []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
    candy.append([0] * m)

candy[0][0] = maps[0][0]

dx = [1, 0, 1]
dy = [0, 1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if candy[nx][ny] < candy[x][y] + maps[nx][ny]:
                candy[nx][ny] = candy[x][y] + maps[nx][ny]


for i in range(n):
    for j in range(m):
        bfs(i, j)

print(candy[-1][-1])
