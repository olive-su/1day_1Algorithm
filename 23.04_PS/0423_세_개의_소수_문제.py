# boj. 11502
# time: 20'

import sys
from math import sqrt
from itertools import combinations_with_replacement

input = sys.stdin.readline
is_prime = [True] * 1001
for i in range(2, int(sqrt(1000)) + 1):
    if is_prime[i]:
        num = 2
        while num * i < 1001:
            is_prime[num * i] = False
            num += 1

primes = []
for i in range(2, 1001):
    if is_prime[i]: primes.append(i)

perm = list(combinations_with_replacement(primes, 3))

def solution():
    k = int(input())
    for a, b, c in perm:
        if a + b + c == k:
            print(a, b, c)
            return 1
    print(0)

for _ in range(int(input())):
    solution()