# Try 1 : 벽 위치에 따른 파이프 이동 불가 조건 파악 못함
# Try 2 : 

import sys

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

ans = 0
# 가로, 대각선, 세로 이동
dx = [1, 1, 0]
dy = [0, 1, 1]

def valid_check(x, y, shape):
    if 0 <= x < n and 0 <= y < n and graph[y][x] != 1:
        if shape == 1:
            if graph[y - 1][x] == 1 or graph[y][x - 1] == 1:
                return False
        return True
    else:
        return False

# shape : row, col, cross
# 시작 위치 : 0, 1, row
def dfs(x, y, shape):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return

    nx, ny, s = x + dx[1], y + dy[1], 1 
    if valid_check(nx, ny, s): dfs(nx, ny, s) 
    if shape == 0 or shape == 1:
        nx, ny, s = x + dx[0], y + dy[0], 0 
        if valid_check(nx, ny, s): dfs(nx, ny, s)
    if shape == 1 or shape == 2:
        nx, ny, s = x + dx[2], y + dy[2], 2 
        if valid_check(nx, ny, s): dfs(nx, ny, s)

dfs(1, 0, 0)
print(ans)
