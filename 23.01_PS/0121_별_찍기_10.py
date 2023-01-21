# boj. 2447
# time : 15' 

import sys

input = sys.stdin.readline
n = int(input())
pattern = [[' ' for _ in range(n)] for _ in range(n)]

dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]

def star(x, y, n):
    if n == 1:
        pattern[y][x] = '*'
        return
    for i in range(9):
        if i == 4: continue
        star(x + dx[i] * n // 3, y + dy[i] * n // 3, n // 3)

star(0, 0, n)

for i in range(n):
    print(''.join(pattern[i]))

