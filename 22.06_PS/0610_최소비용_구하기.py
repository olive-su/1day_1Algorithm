import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

start, end = map(int, input().split())
dijkstra(start)

print(distance[end])
