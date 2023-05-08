# boj. 13549
# time: 

import sys
from heapq import *

input = sys.stdin.readline
n, k = map(int, input().split())
INF = int(1e9)
MAX_SIZE = 100001
time = [INF] * 100001

now = n
time[now] = 0
h = []
heappush(h, (0, now))
while(h):
    t, x = heappop(h) # 시간, 노드 번호
    
    if 0 <= x * 2 < MAX_SIZE and time[x * 2] == INF:
        time[x * 2] = t
        heappush(h, (t, x * 2))
    if 0 <= x + 1 < MAX_SIZE and time[x + 1] == INF:
        time[x + 1] = t + 1
        heappush(h, (t + 1, x + 1))
    if 0 <= x - 1 < MAX_SIZE and time[x - 1] == INF:
        time[x - 1] = t + 1
        heappush(h, (t + 1, x - 1))

print(time[k])




