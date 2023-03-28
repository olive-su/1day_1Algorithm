# boj. 17103
# time: 10' 

import sys

input = sys.stdin.readline
is_prime = [True] * (1000001)
is_prime[0], is_prime[1] = False, False

for i in range(2, 1001):
    num = 2
    if is_prime[i]:
        while num * i <= 1000000:
            is_prime[num * i] = False
            num += 1
    
for _ in range(int(input())):
    t = int(input())
    cnt = 0
    for i in range(2, t // 2 + 1):
        if is_prime[i] and is_prime[t - i]:
            cnt += 1
    print(cnt)

