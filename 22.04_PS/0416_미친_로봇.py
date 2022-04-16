import sys

input = sys.stdin.readline

n, p_e, p_w, p_s, p_n = map(int, input().split())
percent = [p_e/100, p_w/100, p_s/100, p_n/100]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(n * 2 + 1)] for _ in range(n * 2 + 1)]
rst = 0


def dfs(x, y, cnt, p):
    global rst
    if cnt == n + 1:
        rst += p
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, p * percent[i])
            visited[nx][ny] = 0

dfs(0, 0, 0, 1)
print(rst)
