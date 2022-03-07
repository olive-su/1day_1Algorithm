import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
n, m = map(int, input().split())
com = list(combinations_with_replacement(range(1, n+1), m))
for i in com:
    li = list(map(str, i))
    print(' '.join(sorted(li)))
