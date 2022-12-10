# boj. 1303
# time: 13'

import sys
from math import pow
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph, visited = [], []
warrior = {"W" : 0, "B" : 0}

for _ in range(m):
    graph.append(input().rstrip())
    visited.append([False] * n)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x, color):
    cnt = 1
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[ny][nx] and graph[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    cnt += 1
    
    return cnt
            

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            color = graph[i][j] 
            warrior[color] += pow(bfs(i, j, color), 2)

[print(int(i), end=' ') for i in warrior.values()]

