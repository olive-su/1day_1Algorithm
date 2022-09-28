# boj. 1289

import sys
from collections import defaultdict

input = sys.stdin.readline
s, p = map(int, input().split())
string = input()

arr = list(map(int, input().split()))
goal = dict(zip('ACGT', arr))
cnt = defaultdict(int)
answer = 0

for i in range(p):
    cnt[string[i]] += 1

def validation():
    for i in 'ACGT':
        if cnt[i] < goal[i]:
            return 0
    return 1

answer += validation()

for i in range(s-p):
    head, tail = string[i], string[p+i]
    cnt[head] -= 1
    cnt[tail] += 1
    answer += validation()

print(answer)
