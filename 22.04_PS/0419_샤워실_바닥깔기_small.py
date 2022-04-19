import sys

input = sys.stdin.readline
k = 2 ** int(input())
x, y = map(int, input().split())
graph = [[0 for _ in range(k)] for _ in range(k)]
x, y = x - 1, k - y # 좌표 변환
graph[y][x] = -1

# 좌표값 가중치
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]


def daq(a, b, size, cnt):
    flag = 0
    if size == 2:
        for i in range(2):
            for j in range(2):
                if a + j == x and b + i == y:
                    flag = 1
                    continue
                graph[b + i][a + j] = cnt
        return flag
    size = size // 2
    for i in range(4):
        flag = 0
        nx = a + (dx[i]*size)
        ny = b + (dy[i]*size)
        flag = daq(nx, ny, size, cnt)
        if not flag: # 현재 탐색 위치에 배수구가 없을 때 중앙 칸을 비워줌
            graph[ny + dy[(3-i)]][nx + dx[(3-i)]] = 0
        cnt += 1
    return flag

daq(0, 0, k, 1)
for i in range(k):
    for j in range(k):
        if graph[i][j] == 0: # 빈칸일 경우 '5'로 채움 -> 가운데는 반드시 '5'로 채워짐
            print(5, end = ' ')
        else: print(graph[i][j], end = ' ')
    print()

