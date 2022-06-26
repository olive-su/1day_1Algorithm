# boj. 1644

import sys
import math
from collections import deque

input = sys.stdin.readline
n = int(input())
prime = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i] == True:
        num = 2
        while num * i <= n:
            prime[i * num] = False
            num += 1

rst, cnt = 0, 0
q = deque([])
for j in range(n, 1, -1):
    if prime[j] == True:
        if rst < n:
            q.append(j)
            rst += j
        else:
            if len(q) > 0:
                rst -= q.popleft()
                q.append(j)
                rst += j
        if rst == n:
            cnt += 1

print(cnt)
