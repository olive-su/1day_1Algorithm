n = int(input())
dp = [0 for _ in range(101)]

for i in range(0, 4):       
    dp[i] = 1 
for j in range(4, 6):
    dp[j] = 2

for _ in range(n):
    m = int(input())
    for k in range(6, m+1):
        dp[k] = dp[k-1] + dp[k-5] 
    print(dp[m])
