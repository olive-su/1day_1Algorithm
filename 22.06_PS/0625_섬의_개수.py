# boj. 4963

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
w, h = map(int,input().split())

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def dfs(x, y, island, visited):
    visited[y][x] = 1
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if island[ny][nx] and not visited[ny][nx]:
                dfs(nx, ny, island, visited)
    return 1

while (w, h) != (0, 0):
    island, visited = [], []
    cnt = 0

    for _ in range(h):
        island.append(list(map(int, input().split())))
        visited.append([0] * w)
    
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and island[i][j]:
                cnt += dfs(j, i, island, visited)
                
    print(cnt)
    w, h = map(int,input().split())
