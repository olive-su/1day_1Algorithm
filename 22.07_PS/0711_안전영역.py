# boj. 2468

import sys
from collections import deque

input = sys.stdin.readline
rst = 0
n = int(input())
graph = []
max_h = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))
    max_h = max(max_h, max(graph[-1])) # 최대 높이

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x, now, visited):
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and graph[ny][nx] > now:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

for i in range(max_h): # i : 비가 온 양(최대 높이까지 _ 다 잠기는 경우)
    cnt = 0
    visited = [([0] * n) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0 and graph[j][k] > i:
                cnt += 1
                bfs(j, k, i, visited)
    rst = max(rst, cnt)

print(rst)
