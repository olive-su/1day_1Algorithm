# boj. 18513

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count, answer = 0, 0
visited_dict = {}

queue = deque()
for a in arr:
    queue.append(a)
    visited_dict[a] = 0

while queue:
    q = queue.popleft()
    for x in [-1, 1]:
        if visited_dict.get(q + x) == None:
            visited_dict[q + x] = visited_dict[q] + 1
            answer += visited_dict[q] + 1
            queue.append(q + x)
            count += 1
        if count >= k: 
            sys.exit(print(answer))