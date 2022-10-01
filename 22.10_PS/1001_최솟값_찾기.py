# boj. 11003

import sys
from collections import deque

input = sys.stdin.readline
n, l = map(int, input().split())
arr = list(map (int, input().split()))
answer = str(arr[0])
v = deque([(0, arr[0])])

for i in range(1, len(arr)):
    if v[0][0] <= i - l:
        v.popleft()
    while len(v) > 0 and v[-1][1] >= arr[i]:
        v.pop()
    v.append((i, arr[i]))
    answer += ' ' + str(v[0][1])

print(answer)
