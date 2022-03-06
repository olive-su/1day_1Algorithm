# 초기 상태 -> -(1) -> 모든 칸 폭탄 설치(2) -> 폭탄 터짐(3) ->
# n = 짝수 : 모든 칸 폭탄
from hmac import new
from sys import stdin
from collections import deque

r, c, n = map(int, stdin.readline().split())
bombs, new_bombs = [], []


for _ in range(r):
    bombs.append(list(stdin.readline().rstrip()))


def print_maps(bombs, flag=0):  # 격자판 출력 함수
    if flag == 1:
        for i in range(len(bombs)):
            bombs[i] = ['O' * c]
    elif flag == 2:
        for i in range(len(bombs)):
            for j in range(c):
                if bombs[i][j] == '.':
                    print('O', end='')
                else:
                    print('.', end='')
            print('')
    else:
        for i in range(len(bombs)):
            print(''.join(bombs[i]))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)])
    x, y = queue.popleft()
    new_bombs[x][y] = '.'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        new_bombs[nx][ny] = '.'


if n == 1:
    print_maps(bombs)
elif n % 2 == 0:  # 짝수 초
    print_maps(bombs, 1)
    print_maps(bombs)
else:
    for _ in range(3, n + 1, 2):
        new_bombs = [['O' for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if bombs[i][j] == 'O':
                    bfs(i, j)
        bombs = new_bombs
    print_maps(bombs)
