# boj. 11780
# time : 40' 

import sys

input = sys.stdin.readline
INF = int(1e6)
n = int(input())
m = int(input())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
answer = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: graph[i][j] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    if graph[a][b] > w:
        answer[a][b] = [a, b]
        graph[a][b] = w

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                answer[j][k] = answer[j][i][:-1] + answer[i][k] # 중복 기입 방지

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF: print(0, end = ' ')
        else: print(graph[i][j], end = ' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if not graph[i][j] or graph[i][j] == INF: print(0)
        else: 
            print(len(answer[i][j]), end = ' ')
            for k in answer[i][j]:
                print(k, end = ' ')
            print()

