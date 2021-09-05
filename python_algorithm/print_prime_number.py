import math
from sys import stdin
M, N = map(int, stdin.readline().split())

for i in range(M, N+1):
    flag = 1
    for j in range(2, round(math.sqrt(i))+1):
        if i % j == 0:
            flag = 0
            break
    if i > 1 and flag:
        print(i)
