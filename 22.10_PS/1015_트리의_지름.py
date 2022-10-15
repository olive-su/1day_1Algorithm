# boj. 1167
# DFS

import sys

input = sys.stdin.readline
v = int(input())
tree = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
answer = 0
max_point = 0

for i in range(v):
    edges = list(map(int, input().split()))
    num = edges[0]
    for e in range(1, len(edges) - 1, 2):
        n, w = edges[e], edges[e + 1]
        tree[num].append((n, w))

def dfs(n, cnt):
    global answer
    global max_point

    if cnt > answer:
         max_point = n
         answer = cnt
    visited[n] = True

    for a, b in tree[n]:
        if not visited[a]:
            dfs(a, cnt + b)

    visited[n] = False

dfs(1, 0)
dfs(max_point, 0)

print(answer)
