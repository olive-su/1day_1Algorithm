from sys import stdin
from itertools import combinations
import copy

n, m = map(int, stdin.readline().split())
maps, zeros = [], []
rst = 0 # 최종 0의 개수
for i in range(n):
    maps.append(list(map(int, stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            zeros.append((i, j)) # 조합을 구하기 위해 빈 칸인 경우에만 따로 zeros에 튜플 형태로 담음

# 나올 수 있는 전체 조합을 구해서 comb에 담음
comb = list(combinations(zeros, 3)) # ((a, b), (c, d), (e, f)) 형태

def dfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 1: # 범위를 벗어나는 경우
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2 # 0인 경우 바이러스 퍼뜨리고 dfs 실행
            dfs(graph, nx, ny)
            
for c in comb:
    cnt = 0
    maps_copy = copy.deepcopy(maps) # maps을 for문을 돌며 계속 이용해야 하므로 깊은 복사로 만듦
    for cc in c: # 조합 중 하나의 경우에 대해 벽 설치
        maps_copy[cc[0]][cc[1]] = 1
    for i in range(n):
        for j in range(m):
            # 바이러스가 있으면 해당 구역을 시작으로 바이러스를 퍼뜨리기 위해 dfs 수행
            if maps_copy[i][j] == 2: 
                dfs(maps_copy, i, j)
    for i in maps_copy:
        cnt += i.count(0)
    rst = max(rst, cnt)

print(rst)
