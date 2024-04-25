import sys

input = sys.stdin.readline

MOD = 1_000_000_000
n, k = map(int, input().split())

dp = [[1 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD

print(dp[k - 1][n])
