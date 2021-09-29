from sys import stdin
n = int(stdin.readline())
a = stdin.readline().split()
a = list(map(int, a))
for i in range(n):
    a[i] = [i, a[i]]
a.sort(key = lambda x : x[1])
cnt = 0
b = []
b.append([a[0][0], cnt])
for j in range(1, n):
    if a[j-1][1] != a[j][1]: # 이전 원소와 값이 다를 때만 cnt + 1
        cnt += 1
    b.append([a[j][0], cnt])
b.sort(key = lambda x : x[0])
[print(b[i][1], end=' ') for i in range(n)]
