import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = list(map(sorted, graph))

def dfs(s, answer):
    answer.append(s)
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(i, answer)

def bfs():
    queue = deque([v])
    visited[v] = True
    b_answer.append(v)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                b_answer.append(i)
                visited[i] = True

d_answer, b_answer = [], []
visited = [False for _ in range(n + 1)]
dfs(v, d_answer)
visited = [False for _ in range(n + 1)]
bfs()

[print(i, end=' ') for i in d_answer]
print()
[print(i, end=' ') for i in b_answer]
