import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def atob(n, cnt):
    if n > b:
        return
    if n == b:
        sys.exit(print(cnt))

    atob(n * 2, cnt + 1)
    atob(n * 10 + 1, cnt + 1)

atob(a, 1)

print(-1)
