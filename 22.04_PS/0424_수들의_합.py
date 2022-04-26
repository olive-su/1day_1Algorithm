import sys

input = sys.stdin.readline

s = int(input())
i, total = 0, 0
while total < s:
    i += 1
    total += i
print(i) if total == s else print(i - 1)
