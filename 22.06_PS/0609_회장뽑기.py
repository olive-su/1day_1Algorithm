import sys

input = sys.stdin.readline
INF = int(1e9)
score, candidates = INF, []
n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 점수 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: graph[i][j] = 0

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    flag, personal = 0, 0
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            flag = 1
            break
        personal = max(personal, graph[i][j])
    if flag: continue
    if personal <= score:
        if personal < score:
            candidates = []
        candidates.append(i)
        score = personal

print(score, len(candidates))
[print(i, end = ' ') for i in candidates]
