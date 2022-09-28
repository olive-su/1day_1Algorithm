# boj. 2003

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(n):
    total = 0
    for j in range(i, n):
        total += arr[j]
        if total == m:
            answer += 1

print(answer)