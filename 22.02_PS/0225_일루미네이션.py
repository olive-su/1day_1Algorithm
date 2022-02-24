from sys import stdin
from collections import deque

w, h = map(int, stdin.readline().split())
home = []
for _ in range(h):
    home.append(list(map(int, stdin.readline().split())))
cnt = 0

# 1시 방향부터 시계방향으로
dx = [[-1, 0, 1, 1, 0, -1], [-1, 0, 1, 1, 0, -1]]  # 홀수줄, 짝수줄
dy = [[1, 1, 1, 0, -1, 0], [0, 1, 0, -1, -1, -1]]


def bfs(x, y):
    queue = deque([(x, y)])
    home[x][y] = 2
    cnt = 0
    while queue:
        x, y = queue.popleft()
        one = 6
        for i in range(6):
            nx = x + dx[x % 2][i]
            ny = y + dy[x % 2][i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if home[nx][ny]:
                one -= 1
                if home[nx][ny] == 1:
                    home[nx][ny] = 2
                    queue.append((nx, ny))
        cnt += one
    return cnt


def bfs2(x, y):
    queue = deque([(x, y)])
    home[x][y] = 3
    cnt = 0
    flag = 0
    while queue:
        x, y = queue.popleft()
        # one = 6
        for i in range(6):
            nx = x + dx[x % 2][i]
            ny = y + dy[x % 2][i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                flag = 1
                continue
            if home[nx][ny] == 2:
                cnt += 1
            if home[nx][ny] == 0:
                # one -= 1
                home[nx][ny] = 3
                queue.append((nx, ny))
    if flag:
        return 0
    else:
        return cnt


for i in range(h):
    for j in range(w):
        if home[i][j] == 1:
            cnt += bfs(i, j)


for i in range(h):
    for j in range(w):
        if home[i][j] == 0:
            cnt -= bfs2(i, j)

print(cnt)

