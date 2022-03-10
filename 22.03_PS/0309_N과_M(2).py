import sys
from itertools import *

input = sys.stdin.readline
n, m = map(int, input().split())
com = list(combinations(range(1, n+1), m))
for i in com:
    li = list(map(str, i))
    print(' '.join(sorted(li)))

