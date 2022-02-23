from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
com = [[] for _ in range(n + 1)]
max_ans = 0
ans = []

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    com[y].append(x)


def bfs(num):
    visited = [False for _ in range(n + 1)]
    rst = 0
    queue = deque()
    queue.append(num)
    visited[num] = True
    while queue:
        hack = queue.popleft()
        for j in com[hack]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True  # 방문처리
        rst += 1
    return rst


for i in range(1, n + 1):
    if com[i]:
        new = bfs(i)
        if new == max_ans:
            ans.append(i)
        elif new > max_ans:
            ans = [i]
            max_ans = new

[print(ans[i], end=' ') for i in range(len(ans))]

