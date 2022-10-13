# boj. 13023

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num, cnt):
    if cnt >= 5:
        sys.exit(print(1))
    
    visited[num] = True
    for i in graph[num]:
        if not visited[i]:
            dfs(i, cnt + 1)
    visited[num] = False

for i in range(n):
    dfs(i, 1)

print(0)