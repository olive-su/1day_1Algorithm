import sys
from itertools import combinations

input = sys.stdin.readline
arr = list(input().split())
while arr[0] != '0':
    comb = list(combinations(arr[1:], 6))
    for c in comb:
        print(' '.join(c))
    print()
    arr = list(input().split())
