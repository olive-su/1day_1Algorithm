# boj. 17144
# 60'
'''
확산양 : int((origin)/5)
남은양 : (origin) - (확산양 * 개수)
알고리즘 순서 : 확산 -> 순환
'''

import sys
import copy

input = sys.stdin.readline
r, c, t = map(int, input().split())
graph, clean = [], [] # 공기청정기 위치

for i in range(r):
    graph.append(list(map(int, input().split())))
    if graph[-1][0] == -1:
        clean.append(i)

# 동남서북 - 시계방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def spread(x, y, arr, graph):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if graph[ny][nx] != -1: # 확산
                arr[ny][nx] += int(graph[y][x] / 5)
                cnt += 1
    arr[y][x] += (graph[y][x] - int(graph[y][x] / 5) * cnt)
    
    return arr

def rotation(graph):
    arr = copy.deepcopy(graph)

    x, y = 0, clean[1]
    rot = 0
    # 시계방향 회전
    while True:
        nx, ny = x + dx[rot], y + dy[rot]
        if 0 <= nx < c and 0 <= ny < r:
            if (nx, ny) == (0, clean[1]):
                break
            arr[ny][nx] = graph[y][x]
            x, y = nx, ny
        else:
            rot += 1

    x, y = 0, clean[0]
    rot = 0
    # 반시계방향 회전
    while True:
        nx, ny = x + dx[rot], y + dy[rot]
        if 0 <= nx < c and 0 <= ny < r:
            if (nx, ny) == (0, clean[0]):
                break
            arr[ny][nx] = graph[y][x]
            x, y = nx, ny
        else:
            rot -= 1
    
    arr[clean[0]][1], arr[clean[1]][1] = 0, 0
    return arr



for _ in range(t):
    arr = [([0] *  c) for _ in range(r)]
    arr[clean[0]][0], arr[clean[1]][0] = -1, -1
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                arr = spread(j, i, arr, graph)

    graph = rotation(arr)

rst = 2
for i in range(r):
    for j in range(c):
        rst += graph[i][j]

print(rst)