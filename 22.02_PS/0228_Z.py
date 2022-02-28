from sys import stdin, exit
n, r, c = map(int, stdin.readline().split())


def z(n, x, y, total):  # n : 2제곱, (x, y) : 가운데 좌표
    if n == 1:
        if x - 1 == r and y == c:
            total += 1
        elif x == r and y - 1 == c:
            total += 2
        elif x == r and y == c:
            total += 3
        print(total)
        exit()
    else:
        if r < x and c < y:  # 2사분면
            z(n-1, x - 2**(n-1) // 2, y - 2**(n-1) // 2, total)
        elif r < x and c >= y:  # 1사분면
            z(n-1, x - 2**(n-1) // 2, y + 2**(n-1) // 2, total + 4 ** (n-1))
        elif r >= x and c < y:  # 3사분면
            z(n-1, x + 2**(n-1) // 2, y - 2**(n-1) // 2, total + 4 ** (n-1) * 2)
        else:  # 4사분면
            z(n-1, x + 2**(n-1) // 2, y + 2**(n-1) // 2, total + 4 ** (n-1) * 3)


z(n, (2**n // 2), (2**n // 2), 0)

