from sys import stdin
n = int(stdin.readline())
if n == 1:
    print(1)
    exit()
dp = [0] * (n + 1)  # dp 테이블 생성
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[-1] % 10007)
