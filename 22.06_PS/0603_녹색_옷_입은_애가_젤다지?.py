import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def solution(n):
    graph, check = [], []
    for _ in range(n):
        graph.append(list(map(int, input().split()))) # 그래프 입력 받음
        check.append([INF] * n)
    
    q = []
    heappush(q, (graph[0][0], 0, 0))
    check[0][0] = graph[0][0]
    while q:
        dist, x, y = heappop(q)
        if check[y][x] < dist:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[ny][nx]
                if cost < check[ny][nx]:
                    check[ny][nx] = cost
                    heappush(q, (cost, nx, ny))
    
    print(check[n-1][n-1])

n = int(input())
num = 1
while n != 0:
    print("Problem {0}:".format(num), end=' ')
    solution(n)
    num += 1
    n = int(input())
