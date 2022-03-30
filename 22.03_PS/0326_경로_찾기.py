import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
edge = [[] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            edge[i].append(j)  # i -> j 간선 있음을 나타냄


def bfs(start, x):
    queue = deque()
    queue += x
    while queue:
        x = queue.popleft()
        if graph[start][x] == 0:  # 미방문 경로시 방문
            graph[start][x] = 1
            queue += edge[x]


for i in range(n):
    if edge[i]:
        bfs(i, edge[i])
    [print(j, end=' ') for j in graph[i]]
    print()

