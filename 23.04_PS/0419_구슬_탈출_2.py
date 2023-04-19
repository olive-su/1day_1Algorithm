# boj. 13460
# time: timeout

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 상하좌우
rst = 0
red, blue = 0, 0 # y, x

for i in range(n):
    n_input_list = list(input().rstrip())
    graph.append(n_input_list)
    for j in range(m):
        if graph[i][j] == 'R': 
            red = (i, j)
            graph[i][j] = '.'
        if graph[i][j] == 'B': 
            blue = (i, j)
            graph[i][j] = '.'

# 홍/청, 구멍, 현재 내 좌표, 다른 색 구슬 좌표, 방향
def rolling(color, check, now, other, i): 
    y, x = now
    other_y, other_x = other
    while 0 < y + dy[i] < n - 1 and 0 < x + dx[i] < m - 1 and graph[y + dy[i]][x + dx[i]] != '#':
        y, x = y + dy[i], x + dx[i]
        if graph[y][x] == 'O': # 구멍
            check[color] = True
            break
        if y == other_y and x == other_x: # 다른 공 만났을 때
            y, x = y - dy[i], x - dx[i]
            break
    return y, x

queue = deque([(red, blue, rst)])

rr = 0
while queue:
    rr += 1
    red, blue, cnt = queue.popleft()

    if cnt > 9: continue
    ry, rx = red
    by, bx = blue
    for i in range(4):
        check = [False, False] # 구멍 도착 (red, blue)

        if (0 < ry + dy[i] < n - 1 and 0 < rx + dx[i] < m - 1 and graph[ry + dy[i]][rx + dx[i]] != '#') or ( 0 < by + dy[i] < n - 1 and 0 < bx + dx[i] < m - 1 and graph[by + dy[i]][bx + dx[i]] != '#'):
            if abs(ry + dy[i] - by) < abs(ry - by) or abs(rx + dx[i] - bx) < abs(rx - bx): # blue 먼저 굴러야하는 상황
                nby, nbx = rolling(1, check, (by, bx), (ry, rx), i)
                nry, nrx = rolling(0, check, (ry, rx), (nby, nbx), i)
            else:
                nry, nrx = rolling(0, check, (ry, rx), (by, bx), i)
                nby, nbx = rolling(1, check, (by, bx), (nry, nrx), i)
            if not check[1]:
                if check[0]:
                    sys.exit(print(cnt + 1))
                queue.append(((nry, nrx), (nby, nbx), cnt + 1))
print(-1)
