from sys import stdin
t = int(stdin.readline())
d = [0] * 12
d[1], d[2], d[3] = 1, 2, 4
for i in range(4, 12):
    d[i] = d[i-3] + d[i-2] + d[i-1]

for _ in range(t):
    n = int(stdin.readline())
    print(d[n])
