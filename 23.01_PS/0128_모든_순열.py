import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
per = list(permutations(range(1, n + 1), n))
for p in per:
    for i in p:
        print(i, end = ' ')
    print()
