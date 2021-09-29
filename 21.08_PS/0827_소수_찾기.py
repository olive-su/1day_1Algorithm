import math
from sys import stdin
stdin.readline()
input_num = list(map(int, stdin.readline().split()))

# 소수리스트 구하기
arr = [i for i in range(2, 1001)]
for i in range(2, round(math.sqrt((1000)))):
    j = 0
    while j <= len(arr) - 1:
        if arr[j] > i and arr[j] % i == 0:
            arr.remove(arr[j])
        j += 1
cnt = 0
for k in input_num:
    if k in arr:
        cnt += 1
print(cnt)
