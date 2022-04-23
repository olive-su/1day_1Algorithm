import sys
from decimal import Decimal

input = sys.stdin.readline
percent = list(map(int, input().split()))
percent.reverse()
win = [[0 for _ in range(8)] for _ in range(8)]
rst = [[Decimal(0)] * 8 for _ in range(3)]

for i in range(8, 1, -1):
    a  = 8 - i
    for j in range(a+1, 8):
        t = percent.pop()
        win[a][j] = Decimal(t / 100)
        win[j][a] = Decimal(abs(100 - t) / 100)
for i in range(8):
    if i % 2: rst[0][i] = win[i][i - 1]
    else: rst[0][i] = win[i][i + 1]
for i in range(8):
    if i < 2:
        p1, p2 = win[i][2] * rst[0][2], win[i][3] * rst[0][3]
    elif i < 4:
        p1, p2 = win[i][0] * rst[0][0], win[i][1] * rst[0][1]
    elif i < 6:
        p1, p2 = win[i][6] * rst[0][6], win[i][7] * rst[0][7]
    else:
        p1, p2 = win[i][4] * rst[0][4], win[i][5] * rst[0][5]
    rst[1][i] = rst[0][i] * (p1 + p2)

for i in range(8):
    if i < 4:
        p1 = rst[1][4] * win[i][4]
        p2 = rst[1][5] * win[i][5] 
        p3 = rst[1][6] * win[i][6] 
        p4 = rst[1][7] * win[i][7] 
    else:
        p1 = rst[1][0] * win[i][0] 
        p2 = rst[1][1] * win[i][1] 
        p3 = rst[1][2] * win[i][2] 
        p4 = rst[1][3] * win[i][3] 
    rst[2][i] = str(rst[1][i] * (p1 + p2 + p3 + p4))
    
[print(i, end = ' ')for i in rst[2]]