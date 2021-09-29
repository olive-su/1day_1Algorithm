def chess_fill(n, m, chess_arr):
    w_cnt, h_cnt, color = 0, 0, 'W'
    for i in range(n, n+8):
        for j in range(m, m+8):
            if chess_arr[i][j] != color:
                w_cnt += 1
            if color == 'W': color = 'B'
            else: color = 'W'
        if color == 'W': color = 'B'
        else: color = 'W'
    color = 'B'
    for i in range(n, n+8):
        for j in range(m, m+8):
            if chess_arr[i][j] != color:
                h_cnt += 1
            if color == 'W': color = 'B'
            else: color = 'W'
        if color == 'W': color = 'B'
        else: color = 'W'
    return (min(w_cnt, h_cnt))

import sys
input = list(map(int, sys.stdin.readline().split()))
N, M = input[0], input[1]
chess_arr, min_value = [], []
for _ in range(N):
    chess_arr.append(sys.stdin.readline().rstrip())
for i in range(N-7):
    for j in range(M-7):
        min_value.append(chess_fill(i, j, chess_arr))
print(min(min_value))
