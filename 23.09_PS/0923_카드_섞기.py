import sys

input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
init = list(range(3)) * (n // 3)
now = list(range(3)) * (n // 3)
ans = 0

if p == now:
    print(0)
    exit()

while True:
    tmp = []
    for i in s:
        tmp.append(now[i])
    now = tmp
    ans += 1

    if init == now or p == now:
        break

if init == now:
    print(-1)
else:
    print(ans)
