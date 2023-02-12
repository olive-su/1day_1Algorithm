# boj. 3020
# time:

import sys
from heapq import *

input = sys.stdin.readline
n, h = map(int, input().split())
barrier = []
area = [[0 for _ in range(n)] for _ in range(h)]
# print(area)
for i in range(n):
    t = int(input())
    if i % 2 == 0: s, f, t = 0, t, 1
    else: s, f, t = h - 1, h - t - 1, -1
    for j in range(s, f, t):
        area[j][i] = 1

min_v, cnt = 0, 1
rst = []
for i in area:
    heappush(rst, i.count(1))

min_v = heappop(rst)
while True:
    t = heappop(rst)
    if t > min_v: break
    cnt += 1

print(min_v, cnt, sep=' ')



# while start <= end:
#     mid = (start + end) // 2
#     start_count = area[start].count(1)
#     end_count = area[end].count(1)
#     print(start_count, end_count)
#     if end_count < start_count:
#         start = start + 1
#         min_v, cnt = end_count, 1
#     elif end_count == start_count:
#         start = start + 1
#         min_v, cnt = end_count, cnt + 1
#     else:
#         end = end - 1
#         min_v, cnt = start_count, 1


# print(area)
# print(end)
# print(start)
# print(start_count, end_count)

