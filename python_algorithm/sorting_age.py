a, n = [], int(input())
for _ in range(n):
    b = input().split()
    a.append((int(b[0]), b[1]))
a.sort(key=lambda x : x[0])
for i in a: print(i[0], i[1], sep=' ')
