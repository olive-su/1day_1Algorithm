import sys

input = sys.stdin.readline
n = int(input())
rst, arr = 0, []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
while len(arr) > 2:
    rst += arr.pop()
    rst += arr.pop()
    arr.pop()

rst += sum(arr)
print(rst)
