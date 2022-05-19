import sys

input = sys.stdin.readline
arr = []
rst, tip = 0, 1
n = int(input())

for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

for i in arr:
    money = i - (tip - 1)
    if money > 0: rst += money
    tip += 1

print(rst)