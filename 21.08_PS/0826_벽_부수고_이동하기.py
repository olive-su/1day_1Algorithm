from collections import deque
from sys import stdin
n, m = map(int, stdin.readline().split())
graph = []
for i in range(n):
  graph.append(list(map(int, stdin.readline().rstrip())))
block = [[0 for i in range(m)] for j in range(n)]
print(block)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 1:
        if block[nx][ny]: continue
        block[nx][ny] = 1
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

print(bfs(0, 0))
