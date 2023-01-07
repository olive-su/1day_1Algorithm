# boj. 14382
# time: 10'

import sys

input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    n = int(input())
    number_set = set()
    rst = "INSOMNIA"
    for j in range(1, 100):
        m = n * j
        while m > 0:
            number_set.add(m % 10)
            m //= 10
        if len(number_set) >= 10:
            rst = str(n * j)
            break

    print("Case #{}: {}".format(i, rst))