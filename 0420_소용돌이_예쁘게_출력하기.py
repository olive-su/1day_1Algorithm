import sys

input = sys.stdin.readline
r1, c1, r2, c2 = map(int, input().split())
len_r = abs(r1 - r2) + 1
len_c = abs(c1 - c2) + 1
arr = [[0 for _ in range(len_c)] for _ in range(len_r)]
cnt, num, repeat = 0, 2, 1 # 저장한 횟수, 현재 저장할 숫자
x, y = 0, 0
max_len = 0

# 방향 벡터(반시계 방향 우,상,좌,하 순)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
nd = 0

def check(x, y, num):
    global max_len
    if r1 <= y <= r2 and c1 <= x <= c2:
        arr[y - r1][x - c1] = num
        len_num = len(str(num))
        if len_num > max_len:
            max_len = len_num
        return 1
    else: return 0

cnt += check(0, 0, 1)

while cnt < (len_r * len_c):
    for i in range(repeat):
        x = x + dx[nd]
        y = y + dy[nd]
        cnt += check(x, y, num)
        num += 1
    if nd % 2: repeat += 1
    nd = (nd + 1) % 4

for i in range(len_r):
    for j in range(len_c):
        len_now = len(str(arr[i][j]))
        for _ in range(len_now, max_len):
            print(' ', end = '')
        print(arr[i][j], end = ' ')
    print()