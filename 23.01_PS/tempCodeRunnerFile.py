# boj. 1017
# time : 

import sys
from math import *
from time import time

st= time()

input = sys.stdin.readline
answer = []
is_prime = [True] * 2001
is_prime[0], is_prime[1] = False, False

for i in range(int(sqrt(2000)) + 1):
    if is_prime[i]:
        num = 2
        while i * num <= 2000:
            is_prime[i * num] = False
            num += 1

n = int(input())
arr = list(map(int, input().split()))
t = arr[0]
arr = sorted(arr[1:]) # 첫번째 원소와 분리 

if t % 2 == 0: flag = True
else: flag = False

def daq(cnt):
    if cnt == n - 1: # 더 이상 쪼갤 수 없을 때
        return True

    for i in range(n - 1): # 타깃 값 선정
        if not visited[i]:
            t = arr[i]
            ti = i
            visited[i] = True
            break
    
    # 홀수 짝수 여부
    if t % 2 == 0: flag = True
    else: flag = False

    for a in range(n - 1):
        if visited[a]: continue
        if flag and arr[a] % 2 == 0: continue
        elif not flag and arr[a] % 2 != 0: continue
        if is_prime[t + arr[a]]:
            visited[a] = True
            if daq(cnt + 2): return True
            visited[a] = False
    
    visited[ti] = False
    
    return False

for a in range(n - 1):
    if flag and arr[a] % 2 == 0: continue
    elif not flag and arr[a] % 2 != 0: continue
    if not is_prime[t + arr[a]]: continue # 소수 아닌 경우 pass
    visited = [False] * (n - 1)    
    visited[a] = True
    if daq(1): # 나머지 배열 처리
        answer.append(arr[a])
    visited[a] = False
et= time()
print(et - st)
[print(a, end=' ') for a in answer] if answer else print(-1)
