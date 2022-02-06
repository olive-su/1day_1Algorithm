from sys import stdin
from collections import deque


def bfs(graph, visited):
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


c = int(stdin.readline())
p = int(stdin.readline())
computers = [[] for _ in range(c + 1)]
visited = [0] * (c + 1)
for _ in range(p):
    x, y = map(int, stdin.readline().split())
    computers[x].append(y)
    computers[y].append(x)
bfs(computers, visited)
print(visited.count(1) - 1)
