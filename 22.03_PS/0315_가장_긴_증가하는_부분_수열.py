import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
d[0] = 1
for a in range(1, n):
    max_v = 0
    for i in range(a):
        if arr[a] > arr[i]:
            max_v = max(max_v, d[i])
    if max_v == 0:
        d[a] = 1
    else:
        d[a] = max_v + 1

print(max(d))
