from sys import stdin

d = []
[d.append([0, 0, 0]) for _ in range(41)]

def fibo(x):
    if x == 0:
        d[0] = [0, 1, 0]
        return d[0]
    elif x == 1:
        d[1] = [1, 0, 1]
        return d[1]
    if d[x][0] != 0:
        return d[x]
    arr = fibo(x-1)
    a, b, c = arr[0], arr[1], arr[2]
    arr = fibo(x-2)
    a += arr[0]
    b += arr[1]
    c += arr[2]
    d[x] = [a, b, c]
    return d[x]

T = int(input())
for _ in range(T):
    cnt0, cnt1 = 0, 0
    N = int(stdin.readline())
    arr = fibo(N)
    print(arr[1], arr[2])
