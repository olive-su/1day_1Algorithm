#boj. 15686
#time : 40'

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
graph, chicken = [], []

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for a in range(n):
        if arr[a] == 2:
            chicken.append((i, a)) # 치킨집 좌표(y, x)

comb = list(combinations(chicken, m))
rst = int(1e9)
for store in comb:
    answer = 0
    for i in range(n):
        for j in range(n):
            a = int(1e9)
            if graph[i][j] == 1:
                for sy, sx in store:
                    a = min(a, abs(i-sy) + abs(j-sx))
                answer += a
    rst = min(rst, answer)

print(rst)

