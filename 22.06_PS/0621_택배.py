import sys

input = sys.stdin.readline
c, n = map(int, input().split())
cost = []
max_v = 0

for _ in range(n):
    a, b = map(int, input().split())
    cost.append((a, b))
    max_v = max(max_v, b)

dp = [1e9] * (c + max_v + 1) 

cost.sort(key=lambda x : x[1]) # 고객 수 만큼 정렬
for i in range(1, c + max_v + 1): # i : 사람 수
    for j in range(n):
        if cost[j][1] > i: # 정렬했으므로 사람 수가 i를 넘으면 dp 갱신 불가
            break
        if i == cost[j][1]:
            dp[i] = min(cost[j][0], dp[i]) # cost[j][1]값이 처음 등장한 경우
        dp[i] = min(dp[i], dp[i - cost[j][1]]+ cost[j][0])

print(min(dp[c:])) # 적어도 c명이므로 사람수가 c를 넘는 경우도 고려함 