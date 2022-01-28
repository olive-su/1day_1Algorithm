from sys import stdin
from collections import deque
n, m, k, x = map(int, stdin.readline().split())
cities = [[] for _ in range(n + 1)] # 그래프 생성
for _ in range(m): # 입력 받음
    n1, n2 = map(int, stdin.readline().split())
    cities[n1].append(n2)

visited = [-1 for _ in range(n + 1)] # 방문 처리 및 거리 계산을 위한 리스트
visited[x] = 0 # 맨 처음 시작 위치 거리 0으로 설정

def bfs(graph, v, visited):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1 # 이전 위치에서의 거리 + 1
                queue.append(i)

bfs(cities, x, visited)

flag = 1
for i in range(n+1):
    if visited[i] == k:
        print(i)
        flag = 0

if flag: print(-1) # k와 일치하는 거리가 없을 경우 -1 출력
