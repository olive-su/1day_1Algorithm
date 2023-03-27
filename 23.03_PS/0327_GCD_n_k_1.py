# boj. 11689
# time: 25' 

import sys
from math import sqrt

input = sys.stdin.readline
n = int(input())
rst = n

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        rst = rst - rst / i;
        while n % i == 0:
            n /= i;

if (n > 1):
    rst = rst - rst / n;
print(int(rst))

