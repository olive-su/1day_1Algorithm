import sys

x = int(sys.stdin.readline())
a = []
for _ in range(x):
    a.append(int(sys.stdin.readline()))
a.sort()
for i in a: print(i)
