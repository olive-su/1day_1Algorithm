import sys

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = cards[i]
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[i - j] + dp[j])

print(dp[n])

