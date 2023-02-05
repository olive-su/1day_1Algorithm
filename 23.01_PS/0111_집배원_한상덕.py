#boj. 2842
#time: 

import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
graph, emotion = [], []
k_cnt = 0
answer = 0
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

for i in range(n):
    graph.append(input().rstrip())
    for j in range(n):
        if graph[i][j] == 'P': p = (i, j) # y, x
        if graph[i][j] == 'K': k_cnt += 1

for _ in range(n):
    emotion.append(list(map(int, input().split())))

visited = [[-1 for _ in range(n)] for _ in range(n)]

queue = []
# print("k_cnt", k_cnt)
e = emotion[p[0]][p[1]] 
max_v, min_v = e, e
# visited[p[0]][p[1]] = -1 # 출발지 피로도

# p_e = emotion[p[0]][p[1]] # 우체국 피로도
heappush(queue, [0, p[0], p[1]]) # 차이, max, min
while True:
    diff, y, x = heappop(queue)
    if visited[y][x] > -1: continue

    e = emotion[y][x] 
    if e > max_v: val = e - min_v
    elif e < min_v: val = max_v - e
    else: val = max_v - min_v
    
    if diff < val:
        heappush(queue, [val, y, x])
        continue

    if graph[y][x] == 'K': k_cnt -= 1 # 집 카운트 감소
    if k_cnt == 0: break

    visited[y][x] = diff # 방문처리
    max_v = max(max_v, emotion[y][x]) # 최댓값 갱신
    min_v = min(min_v, emotion[y][x]) # 최솟값 갱신

    # print(max_v, min_v)
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == -1:
            e = emotion[ny][nx] 
            if e > max_v: 
                val = e - min_v
            elif e < min_v:
                val = max_v - e
            else: 
                val = max_v - min_v
            heappush(queue, [val, ny, nx]) 


    # gap, e_value, coordinate = heappop(queue)
    # y, x = coordinate[0], coordinate[1]
    # max_e, min_e = e_value[0], e_value[1]
    # max_answer, min_answer = max(max_answer, emotion[y][x]), min(min_answer, emotion[y][x])
    # max_e = max(max_answer, max_e)
    # min_e = min(min_answer, min_e)
    # if gap < max_e - min_e: 
    #     heappush(queue, [max_e - min_e, (max_e, min_e), (y, x)])
    #     continue
    # if visited[y][x] == True: continue
    # visited[y][x] = True
    # if graph[y][x] == 'K':
    #     k_cnt -= 1
    # if k_cnt < 1: 
    #     break
    # for i in range(8):
    #     ny, nx = y + dy[i], x + dx[i]
    #     if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False:
    #         ne_value = (max(max_answer, emotion[ny][nx]), min(min_answer, emotion[ny][nx]))
    #         g=ne_value[0] - ne_value[1]
    #         heappush(queue, [g, ne_value, (ny, nx)])
            
# print(max_v)
# print(min_v)
print(max_v - min_v)

