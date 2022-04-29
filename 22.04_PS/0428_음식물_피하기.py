import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[0 for i in range(m)] for j in range(n)]
ans = 0

for _ in range(k):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    cnt = 1
    queue = deque([(x, y)])
    graph[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = 0
                cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(ans, bfs(j, i))

print(ans)