from sys import stdin
n = int(stdin.readline())
a = []
for _ in range(n):
    b = stdin.readline().split()
    a.append((int(b[0]), int(b[1])))

a.sort(key = lambda x : x[0]) # x좌표 기준 정렬
a.sort(key = lambda x : x[1]) # y좌표 기준 정렬
[print('{} {}'.format(i[0], i[1])) for i in a]
