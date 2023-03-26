# boj. 1016
# time: 50'

import sys
from math import sqrt, pow

input = sys.stdin.readline
min_v, max_v = map(int, input().split())

arr = [True] * (max_v - min_v + 1)
answer = 0

for i in range(2, int(sqrt(max_v)) + 1):
    if pow(i, 2) > max_v: break
    num = min_v // int(pow(i, 2)) + 1 if min_v % int(pow(i, 2)) else min_v // int(pow(i, 2))
    
    while int(pow(i, 2)) * num <= max_v:
        arr[int(pow(i, 2)) * num - min_v] = False
        num += 1

for a in arr:
    if a: answer += 1

print(answer)

