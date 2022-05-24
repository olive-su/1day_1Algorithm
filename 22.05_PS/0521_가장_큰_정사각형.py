# pypy
# dp table, matrix table

import sys

input = sys.stdin.readline
matrix, dp = [], []
n, m = map(int, input().split())
rst = 0

for _ in range(n):
    line = list(map(int, list(input().rstrip())))
    if 1 in line:
        rst = 1
    matrix.append(line)
    dp.append(line)

for i in range(1, n):
    for j in range(1, m):
        k = dp[i-1][j-1] # 대각선에 위치한 칸까지의 가장 큰 정사각형 크기를 구함
        if matrix[i][j] and k: # 현재 칸이 1이고 대각선 칸이 채워진 칸일때
            flag = 0 # 현재 칸으로부터 위 아래로 몇 칸까지 정사각형을 만들 수 있는지 저장
            for r in range(1, k + 1):
                if r < 0 or matrix[i][j - r] == 0 or matrix[i - r][j] == 0:
                    break
                flag += 1
            dp[i][j] = max(dp[i][j], flag + 1)
            rst = max(rst, dp[i][j])

print(rst * rst)



