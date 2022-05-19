# pypy
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
square = [[0 for j in range(m)] for i in range(n)]
rst = 0

def backtracking(y, x):
    global rst

    if (y, x) == (n - 1, m):
        rst += 1
        return
    
    if x == m:
        y, x = y + 1, 0
    
    backtracking(y, x + 1) #넴모 안놓는 경우

    # 넴모 놓을 수 있는 경우
    if x == 0 or y == 0 or square[y - 1][x - 1] == 0 or square[y - 1][x] == 0 or square[y][x - 1] == 0:
        square[y][x] = 1 
        backtracking(y, x + 1)
        square[y][x] = 0
    return

backtracking(0, 0)
print(rst)
