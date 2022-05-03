import sys

input = sys.stdin.readline
n = int(input())
line = []
dp = [1] * n
rst = 0

for i in range(n):
    line.append(list(map(int, input().split())))

line.sort()

for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(n - max(dp))