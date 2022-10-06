# boj. 11399
# 삽입 정렬

import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, n):
    target = arr[i]
    flag = False
    for j in range(i):
        if target < arr[j]:
            arr.insert(j, target)
            flag = True
            break
    if flag:
        arr.pop(i + 1)

for i in range(n):
    answer += sum(arr[:i + 1])

print(answer)
