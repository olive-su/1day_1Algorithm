import sys

input = sys.stdin.readline

turn = []
n, m = map(int, input().split())
lamp = [0] * (m + 1)
for _ in range(n):
    turn.append(list(map(int, input().split())))
    for i in range(1, turn[-1][0] + 1):
        lamp[turn[-1][i]] += 1

# 스위치 하나를 안켰을 때 전부다 킬 수 있는 지 확인
for i in range(n):
    flag = 0
    for j in range(1, turn[i][0] + 1):
        if lamp[turn[i][j]] - 1 == 0:
            flag = 1
            break
    if flag: continue
    else: sys.exit(print(1))

print(0)
