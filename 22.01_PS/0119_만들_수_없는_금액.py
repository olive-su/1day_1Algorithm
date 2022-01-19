import sys
from itertools import combinations

N = int(sys.stdin.readline())
C = list(map(int, list(sys.stdin.readline().split())))
rst = set()

for i in range(1, N + 1):
    comb = list(map(list, combinations(C, i))) # 1개 조합 생성
    comb = list(map(sum, comb)) # 각각 조합에 대한 합 계산
    [rst.add(comb[i]) for i in range(len(comb))] # 집합에 해당 값들 추가

rst = sorted(list(rst))

i = 0

while True: # 1부터 비교하여 없는 값이 나올 경우 해당 값 출력
    if rst[i] != (i + 1): 
        print(i + 1)
        break
    elif (i + 1) == len(rst): # 모든 값 비교할 때까지 없을 경우
        print(i + 2) # 맨 마지막 값에 + 1한 값 출력
        break
    i += 1
