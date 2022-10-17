# boj. 2343

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2
    total, count = 0, 0

    for a in arr:
        if total + a > mid:
            total = 0
            count += 1
        total += a
    
    if total > 0:
        count += 1

    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
