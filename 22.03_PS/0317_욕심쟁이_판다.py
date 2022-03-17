import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
graph, dp = [], []
n = int(input())

for _ in range(n):
    graph.append(list(map(int, input().split())))
    dp.append([1] * n)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
rst = 0


def dfs(x, y):
    if dp[x][y] > 1:
        return dp[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


for i in range(n):
    for j in range(n):
        rst = max(rst, dfs(i, j))

print(rst)
