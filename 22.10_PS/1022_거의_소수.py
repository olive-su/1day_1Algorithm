# boj. 1456

import sys
import math

input = sys.stdin.readline
a, b = map(int, input().split())
c = int(math.sqrt(b))
count = 0
arr = [True] * (c + 1)
arr[0], arr[1] = False, False

# 에라토스테네스의 체(소수인 경우 True)
for i in range(2, int(math.sqrt(c)) + 1):
    num = 2
    if arr[i]:
        while i * num <= c:
            arr[i * num] = False
            num += 1

# 소수 배열에서 거의 소수 탐색
for i in range(2, c + 1):
    if arr[i]:
        num = 2
        while math.pow(i, num) <= b:
            t = math.pow(i, num)
            if t >= a: # 제곱수의 범위가 a이하인 경우는 num 가산만 수행
                count += 1
            num += 1

print(count)
