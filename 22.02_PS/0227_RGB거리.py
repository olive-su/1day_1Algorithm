from sys import stdin

n = int(stdin.readline())
d = [[0, 0, 0] for _ in range(n)]
house = []
for _ in range(n):
    r, g, b = map(int, stdin.readline().split())
    house.append([r, g, b])

d[0] = house[0]

for i in range(1, n):
    for j in range(3):
        d[i][j] = min(d[i-1][(j + 1) % 3], d[i-1][(j + 2) % 3]) + house[i][j]
print(min(d[n-1]))

