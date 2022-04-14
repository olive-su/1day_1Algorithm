import sys
from collections import deque

min_v, max_v = 1, 1e9
rst = min_v
input = sys.stdin.readline
n, m = map(int, input().split())
island = [[] for _ in range(n + 1)]

for _ in range(m): # 각 간선에 따른 중량 표기
    a, b, c = map(int, input().split())
    island[a].append((b, c))
    island[b].append((a, c))

start, end = map(int, input().split()) 

def bfs(w):
    queue = deque(island[start])
    visited[start] = 1
    while queue:
        x, y = queue.popleft()
        if not visited[x] and w <= y: # 미방문시에만 방문
            for i in island[x]:
                queue.append(i)
                visited[x] = 1
    if visited[end]:
        return True
    else: 
        return False

while min_v <= max_v:
    visited = [0 for _ in range(n + 1)] # visted 초기화
    mid = (min_v + max_v) // 2
    if bfs(mid): # mid의 중량으로 end까지 도달 가능할 경우
        rst = mid
        min_v = mid + 1
    else:
        max_v = mid - 1
print(int(rst))