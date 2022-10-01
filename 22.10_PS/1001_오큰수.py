# boj. 17298

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n
stack = [0]

for i in range(1, n):
    target = arr[i]
    while len(stack) and arr[stack[-1]] < target:
        answer[stack.pop()] = target
    stack.append(i)

for a in answer:
    if a == 0:
        print(-1, end=' ')
    else:
        print(a, end=' ')

