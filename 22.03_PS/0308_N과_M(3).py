import sys
from itertools import *

input = sys.stdin.readline
n, m = map(int, input().split())
com = list(product(range(1, n+1), repeat=m))
for i in com:
    li = list(map(str, i))
    print(' '.join(li))
