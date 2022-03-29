
import sys
from itertools import combinations

rst = float('inf')
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    s, b = map(int, input().split())
    rst = min(rst, abs(s - b))
    arr.append((s, b))
for i in range(1, n + 1):
    com = list(combinations(arr, i))
    for j in com:
        sour, bit = 1, 0
        for k in j:
            sour *= k[0]
            bit += k[1]
        rst = min(rst, abs(sour - bit))

print(rst)
