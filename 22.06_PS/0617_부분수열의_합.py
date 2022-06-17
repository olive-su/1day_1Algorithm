import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
com = []
rst = 0

for i in range(1, n + 1):
    com += list(combinations(arr, i))

for c in com:
    if sum(c) == s: rst += 1

print(rst)