# 불통

import sys
from itertools import *

input = sys.stdin.readline
chanel = [str(i) for i in range(10)]
broken = []

n = input().rstrip()
m = int(input())


if m != 0:
    broken = list(input().split())

for b in broken:
    chanel.remove(b)

if len(chanel) == 0:
    sys.exit(print(abs(100 - int(n))))

com = list(product(chanel, repeat = len(n)))

min_num, max_num = '', ''
# 자릿수 - 1 중 가장 작은 수 추가
if len(n) <= 1:
    min_v = None
else:
    for i in range(len(n) - 1):
        min_num += chanel[-1]
    min_v = int(min_num)

if (len(chanel) == 1 and chanel[0] == '0'):
    max_v = None
else:
    for j in range(len(n) + 1):
        if j == 0 and chanel[0] == '0':
            max_num += chanel[1]
        else:
            max_num += chanel[0]
    max_v = int(max_num)

len_n = len(n)
n = int(n)
for c in com:
    rst = ''
    for i in range(len_n):
        rst += c[i]
    rst = int(rst)
    if rst <= n:
        if min_v != None:
            min_v = max(min_v, rst)
    else:
        if max_v != None:
            max_v = min(max_v, rst)

# 차가 더 적은 숫자 지정
if min_v != None:
    if max_v != None:
        if n - min_v > max_v - n:
            num = max_v
        else:
            num = min_v
    else:
        num = min_v
else:
    if max_v != None:
        num = max_v

if min_v == None and max_v == None:
    num = 0
rst = min(abs(num - int(n)) + len(str(num)), abs(100-n))
print(rst)

