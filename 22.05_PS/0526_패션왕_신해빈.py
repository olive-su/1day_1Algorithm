import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cloth = defaultdict(int)
    n = int(input())
    rst = 1
    for _ in range(n):
        name, type = input().split()
        cloth[type] += 1
    for i in cloth.values():
        rst *= (i + 1)
    print(rst - 1)
