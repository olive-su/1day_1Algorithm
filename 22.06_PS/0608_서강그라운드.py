import sys

input = sys.stdin.readline

INF = int(1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items.insert(0, 0)
graph = [([INF] * (n + 1)) for _ in range(n + 1)]
rst = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 자기자신으로 가는 거리 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: 
            graph[i][j] = 0
            graph[j][i] = 0

# 최단 거리 graph에 저장
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost = graph[i][j]
            if cost > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 가장 많은 아이템을 얻을 수 있는 경우 구함
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            cnt += items[j]
    rst = max(cnt, rst)

print(rst)