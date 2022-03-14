from sys import stdin
n = int(stdin.readline())
d = [1, 1]
for i in range(2, n):
    d.append(d[-1] + d[-2])
print(d[-1])
