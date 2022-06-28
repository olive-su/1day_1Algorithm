# boj. 1504

'''
1 -> v1, v2 -> n
1 -> v2, v1 -> n
비교해서 더 짧은 거리 채택
'''

import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())
distance = [([INF] * (n + 1)) for _ in range(n + 1)] # distance[a][b] : a -> b 로 가는 최단 경로
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start][start] = 0
    while q:
        dist, now = heappop(q)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heappush(q, (cost, i[0]))

dijkstra(1)
dijkstra(v1)
dijkstra(v2)

v1_to_v2 = distance[1][v1] + distance[v1][v2] + distance[v2][n] # 1 -> v1, v2 -> n 경로
v2_to_v1 = distance[1][v2] + distance[v2][v1] + distance[v1][n] # 1 -> v2, v1 -> n

rst = min(v1_to_v2, v2_to_v1)

# 그런 경로가 없을 때
if rst >= INF:
    print(-1)
else:
    print(rst)