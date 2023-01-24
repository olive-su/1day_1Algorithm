# boj. 1956
# time : 20'

import sys

input = sys.stdin.readline
INF = int(1e9)
answer = INF
v, e = map(int, input().split())
graph = [[INF for _ in range(v + 1)] for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a][b] = w

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i == j: graph[i][j] = 0

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i != j and graph[i][j] != INF and graph[j][i] != INF:
            answer = min(answer, graph[i][j] + graph[j][i])

print(-1) if answer == INF else print(answer)


