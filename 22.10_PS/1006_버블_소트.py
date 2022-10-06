# boj. 1377
# 버블 정렬

import sys

input = sys.stdin.readline
n = int(input())
original_list = []
sorted_list = []
v = -1e9

for i in range(n):
    original_list.append((int(input()), i))

sorted_list = sorted(original_list)

for i in range(n):
    v = max(v, sorted_list[i][1] - i)

print(v + 1)

