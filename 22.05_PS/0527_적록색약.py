# 적록색약 적용 bfs, 미적용 bfs 두번
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = []
visited_on, visited_off = [], []
cnt_on, cnt_off = 0, 0

for _ in range(n):
    graph.append(input().rstrip())
    visited_on.append([False] * n)
    visited_off.append([False] * n)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def rgb_on(y, x):
    colors = {"R" : "1", "G" : "1", "B" : "0"}
    origin = colors[graph[y][x]]
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited_on[ny][nx] and origin == colors[graph[ny][nx]]:
                    queue.append((ny, nx))
                    visited_on[ny][nx] = True

def rgb_off(y, x):
    origin = graph[y][x]
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited_off[ny][nx] and origin == graph[ny][nx]:
                    queue.append((ny, nx))
                    visited_off[ny][nx] = True

for i in range(n):
    for j in range(n):
        if visited_on[i][j] == False:
            rgb_on(i, j)
            cnt_on += 1
        if visited_off[i][j] == False:
            rgb_off(i, j)
            cnt_off += 1


print(cnt_off, cnt_on)