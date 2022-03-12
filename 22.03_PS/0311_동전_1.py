from sys import stdin

n, k = map(int, stdin.readline().split())

coins = []

for _ in range(n):
    coins.append(int(stdin.readline()))

c = [0] * (k + 1)
c[0] = 1

for i in coins:
    for j in range(i, k + 1):
        c[j] += c[j - i]

print(c[k])
