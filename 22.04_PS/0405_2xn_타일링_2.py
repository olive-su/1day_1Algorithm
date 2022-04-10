from sys import stdin

n = int(stdin.readline())
d = [0, 1, 3]
for i in range(3, n + 1):
    d.append(d[i - 1] + d[i - 2] * 2)
print(d[-1] % 10007) if n > 1 else print(d[1])
