# boj. 14226

import sys
from collections import deque

input = sys.stdin.readline
s = int(input())
visited = [[0 for _ in range(1001)] for _ in range(1001)]

visited[1][0] = 0
queue = deque([(1, 0, 0)])

while queue:
    d, t, c = queue.popleft()
    if d == s: 
        print(t)
        break

    nd, nt, nc = d, t + 1, d
    if 0 <= nd < 1001 and 0 <= nc < 1001 and not visited[nd][nc]: # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        visited[nd][nc] = nt
        queue.append((nd, nt, nc))

    nd, nt, nc = d + c, t + 1, c
    if 0 <= nd < 1001 and 0 <= nc < 1001 and not visited[nd][nc]:  # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        visited[nd][nc] = nt
        queue.append((nd, nt, nc))
    
    nd, nt, nc = d - 1, t + 1, c
    if 0 <= nd < 1001 and 0 <= nc < 1001 and not visited[nd][nc]:  # 화면에 있는 이모티콘 중 하나를 삭제한다.
        visited[nd][nc] = nt
        queue.append((nd, nt, nc))


