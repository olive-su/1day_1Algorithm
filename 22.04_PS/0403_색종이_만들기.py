import sys

input = sys.stdin.readline
n = int(input())
paper = []
cnt = [0, 0]
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]
for _ in range(n):
    paper.append(list(map(int, input().split())))

def check(n, x, y):
    color = paper[x][y]
    flag = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                flag = 1
                break
        if flag: break
    if flag == 0:
        cnt[color] += 1
        return
    for i in range(4):
        nx =  x + (dx[i] * n // 2)
        ny =  y + (dy[i] * n // 2)
        check(n // 2, nx, ny)

check(n, 0, 0)
print(cnt[0])
print(cnt[1])

