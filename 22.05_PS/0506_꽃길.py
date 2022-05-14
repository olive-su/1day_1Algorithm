# 백트래킹

import sys

input = sys.stdin.readline
n = int(input())
flowers, visited = [], []
rst = 1e9
for i in range(n):
    flowers.append(list(map(int, input().split())))
    visited.append([0] * n)

# 중앙, 상, 하, 좌, 우
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]

def backtracking(y, x, total, cnt):
    global rst
    if cnt == 3:
        rst = min(rst, total)
        return
    for i in range(y, n - 1):
        for j in range(x, n - 1):
            flag = 0
            plant = 0
            # 이미 심은 곳인지 검사
            for k in range(5):
                nx, ny = j + dx[k], i + dy[k]
                if visited[ny][nx] == 1: 
                    flag = 1
                    break
            if flag: continue

            # 심을 수 있는 곳 -> 꽃 심음
            for k in range(5):
                nx, ny = j + dx[k], i + dy[k]
                visited[ny][nx] = 1
                plant += flowers[ny][nx]
            backtracking(y, x, total + plant, cnt + 1)
            
            for k in range(5):
                nx, ny = j + dx[k], i + dy[k]
                visited[ny][nx] = 0

for i in range(1, n):
    for j in range(1, n):
        backtracking(i, j, 0, 0)

print(rst)