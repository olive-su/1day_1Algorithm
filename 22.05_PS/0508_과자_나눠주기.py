# pypy 통과

import sys

input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

start, end = 1, arr[-1]

while start <= end:
    cnt = 0
    mid = (end + start) // 2
    for i in arr:
        cnt += (i // mid)
    if cnt >= m:
        start = mid + 1
        ans =  mid
    else:
        end = mid - 1

print(ans)
