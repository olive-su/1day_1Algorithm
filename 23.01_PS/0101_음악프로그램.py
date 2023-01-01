# boj. 2623
# time : 15'

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
answer = []
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(order[0] - 1):
        front = order[i + 1]
        rear = order[i + 2]
        indegree[rear] += 1
        graph[front].append(rear)

queue = deque([])
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    e = queue.popleft()
    answer.append(e)
    for i in graph[e]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)

if len(answer) != n: print(0) # exception
else: [print(a, sep='\n') for a in answer]
