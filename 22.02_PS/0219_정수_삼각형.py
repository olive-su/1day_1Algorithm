from sys import stdin

n = int(stdin.readline())
dp = [0, ]  # dp table
triangle = [0, ]  # 입력값 저장
for i in range(1, n + 1):
    line = list(map(int, stdin.readline().split()))
    triangle.append(line)
    dp.append([0] * i)

dp[1] = [triangle[1][0]]  # [0, [7], [10, 15], ...]
for i in range(2, n + 1):
    for j in range(len(triangle[i])):  # len(triagle[3]) : 3, 8 1 0
        left, right = 0, 0
        if j > 0:
            left = dp[i - 1][j - 1]  # 위층의 좌측 원소
        if j < i - 1:
            right = dp[i - 1][j]  # 위층의 우측 원소
        dp[i][j] = max(left, right) + triangle[i][j]

print(max(dp[n]))
