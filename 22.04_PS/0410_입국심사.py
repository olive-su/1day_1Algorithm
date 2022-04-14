import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ans = 0
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()
start, end = arr[0], arr[-1] * m
while start <= end:
    mid = (start + end) // 2
    rst = 0
    for i in arr:
        rst += mid // i
    if rst < m:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid 

print(ans)