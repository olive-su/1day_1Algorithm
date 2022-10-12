# boj. 11724

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split()) 
    graph[u].append(v)
    graph[v].append(u)

count = 0

def DFS(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            DFS(j)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
