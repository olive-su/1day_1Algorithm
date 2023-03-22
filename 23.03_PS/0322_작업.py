import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph, indegree = [[] for _ in range(n + 1)], [0] * (n + 1)
time = [[] for _ in range(n + 1)] 
queue = deque([])
answer = 0

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    if arr[1]:
        for j in arr[2:]:
            graph[j].append(i)
            indegree[i] += 1

for i in range(1, n + 1):
    if indegree[i] == 0: 
        queue.append(i)

while queue:
    i = queue.popleft()
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0: 
            queue.append(j)
            time[j] += time[i]
            

print(max(time[1:]))



