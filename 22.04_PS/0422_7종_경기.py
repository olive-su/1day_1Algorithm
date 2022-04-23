import sys
import math

input = sys.stdin.readline
a = [9.23076, 1.84523, 56.0211,	4.99087, 0.188807, 15.9803, 0.11193]
b = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
c = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    for i in range(7):
        if i % 3 == 0: # 트랙 경기
            arr[i] = int(a[i] * math.pow((b[i] - arr[i]), c[i]))
        else: # 필드 경기
            arr[i] = int(a[i] * math.pow((arr[i] - b[i]), c[i]))
    print(sum(arr))