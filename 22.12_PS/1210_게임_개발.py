# boj. 1516
#time 40

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
time = [0] * (n + 1) 
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
answer = [0] * (n + 1)

for i in range(1, n + 1):
    l = list(map(int, input().split())) 
    time[i] = l[0]
    for j in l[1:-1]:
        graph[j].append(i) # i로 들어오는 진입 간선 j
        indegree[i] += 1

def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            answer[i] = time[i]
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            answer[i] = max(answer[i], answer[now] + time[i]) # 이전 건물을 짓기까지 걸리는 최대 시간을 더해줘야함
            if indegree[i] == 0:
                q.append(i)

topology_sort()
[print(answer[i]) for i in range(1, n + 1)]


''' 반례 tc
4
20 -1
10 -1
1 1 2 -1
1000 1 2 3 -1

output
20
10
11
1011

answer
20
10
21
1021
'''
