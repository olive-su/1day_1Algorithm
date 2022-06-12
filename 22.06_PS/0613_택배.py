# dijkstra

import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)
graph = []
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
nodes = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # b로 가는 최단 경로 c
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start, 0))
    distance[start][start] = 0 
    while q:
        dist, now, n = heappop(q)
        nodes[start].append(now)
        if distance[start][now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                if now == start:
                    n = i[0]
                distance[start][i[0]] = cost
                nodes[start][i[0]] = n
                heappush(q, (cost, i[0], n))

for i in range(1, n + 1):
    dijkstra(i)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if nodes[i][j] == 0:
            print('-', end=' ')
        else:
            print(nodes[i][j], end=' ')
    print()

