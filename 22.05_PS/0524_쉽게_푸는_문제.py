import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sum, now, num = 0, 1, 1
for i in range(1, m + 1):
    if i >= n:
        sum += now
    num -= 1
    if num == 0: 
        now += 1
        num = now
print(sum)