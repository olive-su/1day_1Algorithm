# boj. 1744

'''
1st 작은 음수 * 2nd 작은 음수
음수 남은 것들 * 0
1st 큰 양수 * 2nd 큰 양수
'''
import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
zero = False
negative = []
positive = []
answer = 0

for _ in range(n):
    t = int(input())
    if t < 0:
        heappush(negative, t)
    elif t > 0:
        heappush(positive, (-t, t))
    else:
        zero = True

while len(negative) > 1:
    a = heappop(negative)
    b = heappop(negative)

    answer += a * b

if zero and len(negative) > 0:
    heappop(negative)

while len(positive) > 1:
    a = heappop(positive)
    b = heappop(positive)

    if a[1] == 1 or b[1] == 1:
        positive.append(a)
        positive.append(b)
        break

    answer += a[1] * b[1]

for p in positive:
    answer += p[1]
answer += sum(negative)

print(answer)





