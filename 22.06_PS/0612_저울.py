import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
items = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    items[a][b] = 1
    items[b][a] = -1

# 자기자신 비교 불가 -> 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            items[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if items[i][j] == INF: # i와 j 대소비교를 할 수 없는 경우
                if items[i][k] != INF and items[k][j] != INF: # i <-> k, k <-> j 대소비교를 할 수 있는 경우 
                    # 대소 관계가 i > k > j 또는 i < k < j 인 경우에만 대소관계 표현 가능
                    if items[i][k] + items[k][j] != 0:
                        items[i][j] = items[i][k]

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if items[i][j] == INF: cnt += 1
    print(cnt)
