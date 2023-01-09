# boj. 14791
# time : 10'

import sys

input = sys.stdin.readline
def is_tidy_number(n):
    for i in range(1, len(n)):
        if int(n[i - 1]) > int(n[i]):
            return False
    return True

for k in range(1, int(input()) + 1):
    n = input().rstrip()
    if is_tidy_number(n):
        print("Case #{}: {}".format(k, n))
        continue
    t = list(n[:])
    for i in range(len(n) - 1, 0, -1):
        t[i] = '9'
        t[i - 1] = str(int(n[i - 1]) - 1)
        if is_tidy_number(t):
            print("Case #{}: {}".format(k, int(''.join(t))))
            break