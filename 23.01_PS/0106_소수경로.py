# boj. 1963
# time: 38'

import sys
from collections import deque

input = sys.stdin.readline
is_prime = [True] * 10000
for i in range(2, 100):
    num = 2
    if is_prime[i]:
        while num * i < 10000:
            is_prime[num * i] = False
            num += 1


for _ in range(int(input())):
    visited = [-1] * 10000
    a, b = map(int, input().split())
    
    visited[a] = 0
    q = deque([a])
    while q:
        m = q.popleft()
        num = list(str(m))
        for i in range(4):
            for j in range(0, 10):
                if num[i] == str(j): continue
                if i == 0 and j == 0: continue

                t = num[:]
                t[i] = str(j)
                target = int(''.join(t))
                if is_prime[target] and visited[target] == -1:
                    q.append(target)
                    visited[target] = visited[m] + 1

    [print("impossible") if visited[b] == -1  else print(visited[b])]

