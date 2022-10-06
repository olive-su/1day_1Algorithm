# boj. 1427
# 선택 정렬

import sys

input = sys.stdin.readline
arr = list(map(int, list(input().rstrip())))

for i in range(len(arr)):
    v = arr[i]
    idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] > v:
            v = arr[j]
            idx = j
    tmp = arr[idx]
    arr[idx] = arr[i]
    arr[i] = tmp

print(''.join(list(map(str, arr))))

