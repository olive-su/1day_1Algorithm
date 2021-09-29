import sys
a, n = [], int(sys.stdin.readline())
for _ in range(n):
    m = sys.stdin.readline().split()
    a.append((int(m[0]), int(m[1])))
a.sort(key=lambda x:x[1])
a.sort(key=lambda x:x[0])
for i in a:
    print(i[0], i[1], sep=' ')
