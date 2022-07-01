# boj. 9205

'''
맨해튼 거리가 제일 적은 곳 방문
'''

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    shop, visited = [], [0, ]
    hx, hy = map(int, input().split()) # 집
    
    for _ in range(n): # 편의점, 페스티벌 위치 저장
        shop.append(tuple(map(int, input().split())))
        visited.append(0)
    fx, fy = map(int, input().split())
    shop.insert(0, (fx, fy))

    def check_candidate(arr, visited):
        rx, ry, ri = 0, 0, 0
        for ax, ay, ai in arr:
            for v in range(len(visited)):
                if not visited[v]: # 미방문 노드 중 다음 노드와의 거리 비교
                    n_dist = abs(ax - shop[v][0]) + abs(ay - shop[v][1])



    def bfs():
        q = deque([(hx, hy)])
        while q:
            x, y = q.popleft()
            dist = 1e9
            nx, ny = 32768, 0
            candidate = []
            for i in range(n + 1):
                n_dist = abs(x - shop[i][0]) + abs(y - shop[i][1])
                if n_dist <= 1000 and not visited[i]:
                    if n_dist < dist: 
                        nx, ny = shop[i][0], shop[i][1]
                        if nx == fx and ny == fy:
                            return True
                        dist = n_dist
                        ni = i
                        candidate = [(nx, ny, i)]
                    elif n_dist == dist:
                        candidate.append((shop[i][0], shop[i][1], i))
            if len(candidate) > 1:
                nx, ny, i = check_candidate(cadidate, visited)

            if nx == 32768:
                return False
            q.append((nx, ny))
            visited[ni] = 1
        return False

    if bfs():
        print('happy')
    else:
        print('sad')
