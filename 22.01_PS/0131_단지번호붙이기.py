from sys import stdin

n = int(stdin.readline())
maps, house = [], []
for i in range(n):
    maps.append(list(map(int, stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    cnt = 1
    maps[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if maps[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt


for i in range(n):
    for j in range(n):
        cnt = 0
        if maps[i][j]:
            house.append(dfs(i, j))
print(len(house))
[print(sorted(house)[i], sep='\n') for i in range(len(house))]
