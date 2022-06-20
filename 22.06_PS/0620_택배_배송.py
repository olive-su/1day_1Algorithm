import sys
from heapq import *

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist: # 이미 최단거리 갱신 완료
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

dijkstra(1)

print(distance[n])
