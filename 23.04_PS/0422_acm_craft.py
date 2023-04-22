# boj. 1005
# time: 13' 

import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    indegree, graph, rst = [0] * (n + 1), [[] for _ in range(n + 1)], [0] * (n + 1)
    queue = deque([])
    for i in range(k):
        a, b = map(int, input().split())
        indegree[b] += 1
        graph[a].append(b)
    target = int(input())

    for i in range(1, n + 1):
        if indegree[i] == 0: 
            queue.append(i)
            rst[i] = time[i]
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            rst[i] = max(rst[i], rst[x])
            indegree[i] -= 1
            if indegree[i] == 0:
                rst[i] += time[i]
                queue.append(i)
    
    print(rst[target])


for _ in range(int(input())):
    solution()


