from sys import stdin
n = int(stdin.readline())
graph = []
d = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
    d.append([0] * n)
d[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        ni = i + graph[i][j]
        nj = j + graph[i][j]
        if ni < n:
            d[ni][j] += d[i][j]
        if nj < n:
            d[i][nj] += d[i][j]

print(d[n-1][n-1])
