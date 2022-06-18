# 플로이드-워셜 반대로 진행
import sys
import copy

input = sys.stdin.readline
n = int(input())
INF = int(1e9)
distance =  []
origin, v = 0, 0
rst = 0
for _ in range(n):
    distance.append(list(map(int, input().split())))
    origin += sum(distance[-1])

# k를 거쳐서 가는 경우가 존재할 경우, distance[i][j]는 굳이 필요 없으므로 제거
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k: continue
            if distance[i][j] != 0:
                if distance[i][k] + distance[k][j] == distance[i][j]:
                    distance[i][j] = INF
                    distance[j][i] = INF

check = copy.deepcopy(distance)

# 최소한의 도로 리스트로 구할 수 있는 최단 거리 다시 구해서 check 리스트에 저장
for k in range(n):
    for i in range(n):
        for j in range(n):
            check[i][j] = min(check[i][k] + check[k][j], check[i][j])

# 불가능한 경우 처리
# 맨 처음 입력으로 주어진 최단 거리가 안나올 경우
for i in range(n):
    for j in range(n):
        if distance[i][j] and distance[i][j] != INF:
            rst += distance[i][j]
            distance[j][i] = 0
        v += check[i][j]

if origin != v:
    print(-1)
else:
    print(rst)