# boj. 2750
# 버블정렬

import sys

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

def swap(arr, x, y):
    if arr[x] > arr[y]:
        arr[x], arr[y] = arr[y], arr[x]
    return arr

for i in range(n, 1, -1):
    for j in range(i - 1):
        arr = swap(arr, j, j + 1)

for i in arr:
    print(i)

