import sys

input = sys.stdin.readline
papers, cnt = [], [0, 5, 5, 5, 5, 5] # 색종이 입력, 잔여 색종이 수
for _ in range(10):
    papers.append(list(map(int, input().split())))
rst = 0

# x, y == 4부터 시작
def dfs(x, y, z):
    global rst

    for i in range(y, y-z, -1):
        for j in range(x, x-z, -1):
            if papers[i][j] == 0 or papers[i][j] > 1: return
    for i in range(y, y-z, -1):
        for j in range(x, x-z, -1):
            papers[i][j] = z + 1
    rst += 1
    cnt[z] -= 1
    return

for p in range(5, 0, -1):
    for i in range(p - 1, 10):
        for j in range(p - 1, 10):
            if cnt[p]: dfs(j, i, p)

for i in range(10):
    for j in range(10):
        if papers[i][j] == 1:
            sys.exit(print(-1))
print(rst)