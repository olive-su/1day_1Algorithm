# pypy

import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
graph, union = [], [[0] * n for _ in range(n)]
turn = 1
days = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))
    union.append([False] * n)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 열린 국경을 union에 저장한다.
def bfs(x, y):
    global turn

    cnt, total = 1, graph[y][x] # cnt: 연합을 이루고 있는 칸의 개수, total: 연합국의 총 인구수
    queue = deque([(x, y)])
    union[y][x] = turn

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(graph[y][x] - graph[ny][nx]) <= r and union[ny][nx] == False:
                    union[ny][nx] = turn
                    cnt += 1
                    total += graph[ny][nx]
                    queue.append((nx, ny))
    return total, cnt

# 인구 이동 결과 반영 함수
def trans(num):
    global turn

    for i in range(n):
        for j in range(n):
            if union[i][j] == turn: # 국경 열린 상태
                graph[i][j] = num

while True:
    flag = 0
    union = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx, ny = j + dx[k], i + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if l <= abs(graph[i][j] - graph[ny][nx]) <= r and union[ny][nx] == False:
                        t, c = bfs(nx, ny) # 국경선을 공유할 수 있는 국가 찾음 -> bfs 진행
                        trans(t // c) # 연합 이후 인구 이동을 한 결과 반영
                        flag = 1
                        turn += 1 # 좌표들끼리의 연결상태를 구분하기 위함
    if flag == 0: break # 더이상 인구이동이 일어날 수 없는 상황
    days += 1

print(days)
