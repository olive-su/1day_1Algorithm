import sys
a = []
n = int(sys.stdin.readline())
for _ in range(n):
    b = int(sys.stdin.readline())
    if b == 0:
        a.pop()
    else: a.append(b)
print(sum(a))
