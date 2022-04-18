import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
friend = [[] for _ in range(n + 1)]
rst = [[1e9 for _ in range(n)] for _ in range(n)]
ans = [1e9, 0]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
def bfs(visited, start):
    queue = deque([])
    for i in friend[start + 1]:
        queue.append((i, 1))
    visited[start] = 1
    while queue:
        x, y = queue.popleft()
        rst[start][x-1] = min(rst[start][x-1], y)
        if visited[x-1] == 0:
            for i in friend[x]:
                queue.append((i, y + 1))
            visited[x-1] = 1

for i in range(n):
    visited = [0] * n
    bfs(visited, i)
    rst[i][i] = 0
    sum_v = sum(rst[i])
    if ans[0] > sum_v:
        ans[0] = sum_v
        ans[1] = i + 1
print(ans[1])

