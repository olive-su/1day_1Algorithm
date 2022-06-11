import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph, visited = [], []
time, now, cnt = 0, 2, [] # 총 시간, 현재 치즈 녹는 거 표시, 개수

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([0] * m)

def bfs(x, y, v):
    cnt = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == -1 and visited[ny][nx] != v:
                    if graph[y][x] != -1:
                        cnt += 1
                    graph[y][x] = -1
                if graph[ny][nx] == 1 and visited[ny][nx] != v:
                    visited[ny][nx] = v
                    q.append((nx, ny))
    return cnt

# 바깥부분 = -1
def hole(x, y, v): 
    flag = False
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == -1:
                    flag = True
                if graph[ny][nx] == 0 and visited[ny][nx] != v:
                    visited[ny][nx] = v
                    if v == -1:
                        graph[ny][nx] = -1
                    q.append((nx, ny))
    return flag

hole(0, 0, -1)
while True:
    flag = 0
    cnt.append(0)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                if hole(j, i, now):
                    hole(j, i, -1)
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                flag = 1
                cnt[-1] += bfs(j, i, now)
    if not flag: break 
    now += 1
    time += 1


print(time)
print(cnt[-2])