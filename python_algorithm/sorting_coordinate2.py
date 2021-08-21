from sys import stdin
n = int(stdin.readline())
a = []
for _ in range(n):
    b = stdin.readline().split()
    a.append((int(b[0]), int(b[1])))

a.sort(key = lambda x : x[0])
a.sort(key = lambda x : x[1])
[print('{} {}'.format(i[0], i[1])) for i in a]
