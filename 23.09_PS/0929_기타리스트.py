# time : 30'
import sys

n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
src = [s]

for i in range(n):
    v = volumes[i]
    dest = []
    while len(src) > 0:
        now = src.pop()
        na = now + v
        nb = now - v
        if (na <= m and na not in dest):
            dest.append(na)
        if (nb >= 0 and nb not in dest):
            dest.append(nb)

    if (len(dest) == 0):
        print(-1)
        sys.exit()
    src = dest

print(max(src))
