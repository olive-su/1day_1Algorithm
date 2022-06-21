import sys
from collections import deque
'''
F: 총 층 수
S: 현재 위치
G: 스타트링크 위치
U: 위로 u층
D: 아래로 d층
'''
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)

def bfs(x):
    q = deque([x])
    visited[x] = 1

    while q:
        nx = 0
        x = q.popleft()
        if x == g:
            return
        else:
            if x + u <= f:
                nx = x + u
                if not visited[nx]:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
            if x - d >= 1:
                nx = x - d
                if not visited[nx]:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    return

bfs(s)

if visited[g] == 0:
    print("use the stairs")
else:
    print(visited[g] - 1)