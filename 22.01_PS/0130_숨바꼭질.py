from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())

time = [0] * 100001


def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            print(time[k])
            return
        for nv in (v - 1, v + 1, v * 2):
            if nv < 0 or nv > 100000 or time[nv]:
                continue
            time[nv] = time[v] + 1
            queue.append(nv)

bfs(n)
