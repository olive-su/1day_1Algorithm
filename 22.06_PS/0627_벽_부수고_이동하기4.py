# boj. 16946

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph, visited, num = [], [], [0, ]
cnt = 1

for _ in range(n):
    graph.append(list(input().rstrip()))
    visited.append([0] * (m))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, cnt):
    q = deque([(x, y)])
    rst = 1
    visited[y][x] = cnt

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == '0' and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = cnt
                    rst += 1
    return rst


# 연결되어 있는 '0'인 칸의 개수를 num 리스트에 저장
# visited에 연결 상태 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0' and visited[i][j] == 0:
            num.append(bfs(j, i, cnt))
            cnt += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1':
            rst = 1
            s = []
            for k in range(4): # 상하좌우 각각에 저장되어 있는 '0'의 개수들 모두 더함
                ni, nj = i + dy[k], j + dx[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if visited[ni][nj] not in s:
                        rst += num[visited[ni][nj]]
                    s.append(visited[ni][nj])
        else:
            rst = 0
        print(rst % 10, end='')
    print()