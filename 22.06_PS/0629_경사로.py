# boj. 14890

import sys

input = sys.stdin.readline
n, l = map(int, input().split())
rst = 0
arr_r = [] # 열 버전
arr_c = [[[] for _ in range(n)] for _ in range(n)] # 행 버전
for i in range(n):
    arr_r.append(list(map(int, input().split())))
    for c in range(n):
        arr_c[c][i] = arr_r[-1][c]

# 높으면 걸어온 길이 l개 연속 등장
# 낮으면 앞으로 걸어길 길이 l개 연속 등장

def road(line):
    cnt = 1
    flag = 0 # 앞으로 걸어갈 길 높이 체크
    for i in range(1, len(line)):
        if abs(line[i - 1] - line[i]) > 1:
            return False
        if line[i - 1] == line[i]:
            cnt += 1
            if flag and cnt == l: # 내리막 경사로 설치
                flag = 0
                cnt = 0
        elif line[i - 1] < line[i]:
            if flag: return False
            if cnt >= l:
                cnt = 1
            else: return False
        elif line[i - 1] > line[i]:
            if flag: return False
            flag = 1 # 지금부터 체크해야함을 알림
            cnt = 1
            if flag and cnt == l: # l이 1인 경우
                flag = 0
                cnt = 0
    if flag: return False
    return True

for i in range(n):
    if road(arr_c[i]):
        rst += 1
    if road(arr_r[i]):
        rst += 1

print(rst)

