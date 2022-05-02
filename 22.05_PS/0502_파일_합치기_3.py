import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    rst = 0
    k = int(input())
    file = list(map(int, input().split()))
    priority_queue = []
    for i in file:
        heapq.heappush(priority_queue, i)
    while len(priority_queue) > 1:
        x, y = heapq.heappop(priority_queue), heapq.heappop(priority_queue)
        total = x + y
        rst += total
        heapq.heappush(priority_queue, total)
    print(rst)