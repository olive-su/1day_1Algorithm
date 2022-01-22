def factorial(n):
    rst = 1
    for i in range(1, n+1):
        rst *= i
    return rst


from sys import stdin
N = int(stdin.readline())
cnt = 0
N = factorial(N)
N = str(N)
for i in range(len(N)-1, -1, -1):
    if N[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break
