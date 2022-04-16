import sys

input = sys.stdin.readline
sudoku = []
empty = []
for _ in range(9):
    sudoku.append(list(input().rstrip()))
for i in range(8, -1, -1):
    for j in range(8, -1, -1):
        if sudoku[i][j] == '0':
            empty.append((i, j))

def rectangle_check(x, y, s):
    d = [[0, 1, 2], [0, -1, 1], [0, -1, -2]]
    for i in d[x % 3]:
        for j in d[y % 3]:
            if s == sudoku[x + i][y + j]:
                return False
    return True

def backtracking(x, y, s):
    if s in sudoku[x]: # 같은 열 탐색
        return False
    for l in range(0, 9):
        if s == sudoku[l][y]: # 같은 행 탐색
            return False
    if rectangle_check(x, y, s) == False: # 9x9 격자 탐색
        return False
    if len(empty) == 0: # 빈칸을 모두 채웠을 경우
        sudoku[x][y] = s
        for i in sudoku:
            print(''.join(i))
        exit()
    nx, ny = empty.pop()
    sudoku[x][y] = s
    for k in range(1, 10):
        ns = str(k)
        backtracking(nx, ny, ns)
    sudoku[x][y] = '0'
    empty.append((nx, ny))
    

x, y = empty.pop()
for k in range(1, 10):
    s = str(k)
    backtracking(x, y, s)
