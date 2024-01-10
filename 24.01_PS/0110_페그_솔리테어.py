# time: 40'

import sys

input = sys.stdin.readline
global ans_pin
global ans_cnt

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution():
    global ans_pin
    global ans_cnt

    board, pin_cnt = [], 0
    for i in range(5):
        line = list(input().rstrip())
        for j in range(9):
            if line[j] == 'o':
                pin_cnt += 1  # y, x
        board.append(line)

    back_tracking(board, pin_cnt, 0)

    return ans_pin, ans_cnt


def back_tracking(board, pin, cnt):
    global ans_pin
    global ans_cnt

    for y in range(5):
        for x in range(9):
            if board[y][x] == 'o':
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < 5 and 0 <= nx < 9 and \
                            0 <= ny + dy[i] < 5 and 0 <= nx + dx[i] < 9 and \
                            board[ny][nx] == 'o' and board[ny + dy[i]][nx + dx[i]] == '.':
                        board[y][x] = '.'
                        board[ny][nx] = '.'
                        board[ny + dy[i]][nx + dx[i]] = 'o'
                        back_tracking(board, pin - 1, cnt + 1)
                        board[y][x] = 'o'
                        board[ny][nx] = 'o'
                        board[ny + dy[i]][nx + dx[i]] = '.'

    if pin < ans_pin:
        ans_pin, ans_cnt = pin, cnt
    return


for _ in range(int(input())):
    ans_pin, ans_cnt = int(1e9), 0
    a, b = solution()
    input()
    print(a, b, sep=' ')
