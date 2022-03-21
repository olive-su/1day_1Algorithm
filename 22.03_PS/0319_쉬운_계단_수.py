from sys import stdin
from copy import *

n = int(stdin.readline())
d1 = [1] * (10)
MOD = 1000000000
d1[0] = 0
for i in range(1, n):
    d2 = [0] * (10)
    for j in range(10):
        if j == 0:
            d2[j] = d1[1]
        elif j == 9:
            d2[j] = d1[8]
            break
        else:
            d2[j] = (d1[j - 1] + d1[j + 1])
    d1 = deepcopy(d2)
print(sum(d1) % MOD)
