# boj. 18428
# time: 27' 

'''
빈칸에 장애물 놓고 combination으로 모든 조합 추출
Maximum : 5984
'''

import sys
from itertools import combinations

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
flag = False
n = int(input())
board = []
empty_space, teacher = [], []

for _ in range(n):
    board.append(input().split())

def monitor(teacher, obstacle): # teacher 좌표, 장애물 좌표
    for y, x in teacher:
        oy, ox = y, x
        for i in range(4):
            # 장애물이면, 선생님이면, 좌표값을 벗어나면 더이상 탐색 필요x
            y, x = oy, ox
            y, x = y + dy[i], x + dx[i]
            while 0 <= y < n and 0 <= x < n and board[y][x] != 'T' and (y, x) not in obstacle:
                if board[y][x] == 'S': # 학생이면
                    return False
                y, x = y + dy[i], x + dx[i]
    return True

for y in range(n):
    for x in range(n):
        if board[y][x] == 'X':
            empty_space.append((y, x)) # 장애물을 놓을 수 있는 공간 파악
        elif board[y][x] == 'T':
            teacher.append((y, x))

comb = list(combinations(empty_space, 3))

for c in comb:
    if monitor(teacher, c):
        flag = True
        break

print('YES') if flag else print('NO')