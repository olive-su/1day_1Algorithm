from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)
for i in range(n):
    t, p = map(int, stdin.readline().split())
    if t > n - i:  # 기간이 남은 근무일보다 긴 경우
        continue
    dp[i] = max(dp[:i+1]) # 현재 인덱스 이전 dp 테이블에서 가장 큰 값이 있을때 (boj 예제4)
    dp[i + t] = max(dp[i] + p, dp[i + t])

print(max(dp))
