
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = int(-1e9)

dp = [[int(-1e9) for _ in range(n)] for _ in range(2)]

dp[0][0] = arr[0]
dp[1][0] = arr[0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
    if dp[1][i - 1] + arr[i] < dp[0][i - 1]:
        dp[1][i] = dp[0][i - 1]
    else:
        dp[1][i] = dp[1][i - 1] + arr[i]

for i in range(2):
    ans = max(ans, max(dp[i]))

print(ans)
