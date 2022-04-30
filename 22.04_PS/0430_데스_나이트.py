import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
chess = [[-1 for _ in range(n)] for _ in range(n)]

r1, c1, r2, c2 = map(int, input().split())

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

def bfs():
    queue = deque([(r1, c1)])
    chess[c1][r1] = 0
    while queue:
        r, c = queue.popleft()
        for i in range(6):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if chess[nc][nr] == -1:
                    chess[nc][nr] = chess[c][r] + 1
                    queue.append((nr, nc))

bfs()
print(chess[c2][r2])