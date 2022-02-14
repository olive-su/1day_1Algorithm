from sys import stdin
x = int(stdin.readline())

if x < 4:
    d = [0] * 4
else:
    d = [0] * (x + 1)
d[1], d[2], d[3] = 0, 1, 1

for i in range(4, x + 1):
    v = i + 1
    if i % 3 == 0:
        v = min(v, d[i // 3])
    if i % 2 == 0:
        v = min(v, d[i // 2])

    v = min(v, d[i - 1])

    d[i] = v + 1

print(d[x])

