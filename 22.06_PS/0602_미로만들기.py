from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return print(visited[x][y] - 1)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

bfs()