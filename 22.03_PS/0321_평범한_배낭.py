from sys import stdin
n, k = map(int, stdin.readline().split())

arr = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(k + 1):
        if j < w:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - w] + v)

print(arr[n][k])
