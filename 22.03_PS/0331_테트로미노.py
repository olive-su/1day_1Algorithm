import sys
sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[0 for j in range(m)] for i in range(n)]
v = [[0 for j in range(m)] for i in range(n)]
global rst
rst = 0
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, step, total):
    global rst
    if step == 4:
        rst = max(rst, total)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        visited[x][y] = 1
        dfs(nx, ny, step + 1, total + graph[nx][ny])
        visited[x][y] = 0


def dfs_cross(x, y):
    global rst
    start = graph[x][y]
    if x - 1 >= 0 and x + 1 < n and y - 1 >= 0:  # ㅓ
        rst = max(rst, start + graph[x-1][y] + graph[x+1][y] + graph[x][y-1])
    if x - 1 >= 0 and y - 1 >= 0 and y + 1 < m:  # ㅗ
        rst = max(rst, start + graph[x-1][y] + graph[x][y-1] + graph[x][y+1])
    if x - 1 >= 0 and x + 1 < n and y + 1 < m:  # ㅏ
        rst = max(rst, start + graph[x-1][y] + graph[x+1][y] + graph[x][y+1])
    if x + 1 < n and y - 1 >= 0 and y + 1 < m:  # ㅜ
        rst = max(rst, start + graph[x+1][y] + graph[x][y-1] + graph[x][y+1])


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0
        dfs_cross(i, j)

print(rst)
