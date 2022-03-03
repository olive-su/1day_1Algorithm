import sys

input = sys.stdin.readline
n = int(input())
d = [0] * 3
d[0], d[1] = 1, 2

for i in range(3, n + 1):
    d[2] = (d[0] + d[1]) % 15746
    d[0] = d[1]
    d[1] = d[2]

if n < 3:
    print(d[n-1])
else:
    print(d[-1])
