import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(origin, target, n, graph):
    x, y = origin
    tx, ty = target
    q = deque([(x, y)])
    graph[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == -1: # 미방문
                    q.append((nx, ny))
                    graph[ny][nx] = graph[y][x] + 1
                    if nx == tx and ny == ty:
                        return
        

for _ in range(t):
    n = int(input())
    graph = [[-1 for _ in range(n)]for _ in range(n)]
    sx, sy = map(int, input().split()) # start 
    ex, ey = map(int, input().split()) # end
    bfs((sx, sy), (ex, ey), n, graph)
    print(graph[ey][ex])
