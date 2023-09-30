# time : 35'

import sys
import copy

input = sys.stdin.readline
r, c, t = map(int, input().split())

graph = []
machine = []
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
left_x = [1, 0, -1, 0]
left_y = [0, -1, 0, 1]
right_x = [1, 0, -1, 0]
right_y = [0, 1, 0, -1]

for i in range(r):
    graph.append(list(map(int, input().split())))
    if (graph[i][0] == -1):
        machine.append(i)


def spread(g):
    new_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if g[i][j] == -1:
                new_graph[i][j] = -1
                continue
            if g[i][j]:
                unit = g[i][j] // 5
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < r and 0 <= nx < c and g[ny][nx] != -1:
                        new_graph[ny][nx] += unit
                        g[i][j] -= unit
                new_graph[i][j] += g[i][j]
    return new_graph


def clean(g):
    new_graph = copy.deepcopy(g)

    y, x = machine[0], 0
    g[y][x] = 0
    for i in range(4):
        ny, nx = y + left_y[i], x + left_x[i]
        while 0 <= ny < r and 0 <= nx < c and (ny != machine[0] or nx != 0):
            new_graph[ny][nx] = g[y][x]
            y, x = ny, nx
            ny, nx = y + left_y[i], x + left_x[i]

    y, x = machine[1], 0
    g[y][x] = 0
    for i in range(4):
        ny, nx = y + right_y[i], x + right_x[i]
        while 0 <= ny < r and 0 <= nx < c and (ny != machine[1] or nx != 0):
            new_graph[ny][nx] = g[y][x]
            y, x = ny, nx
            ny, nx = y + right_y[i], x + right_x[i]
    return new_graph


for i in range(t):
    graph = spread(graph)
    graph = clean(graph)

total = 0
for i in range(r):
    for j in range(c):
        total += graph[i][j]
print(total + 2)
