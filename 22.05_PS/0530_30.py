# 각 자리수의 합이 3의 배수이면서 맨 마지막이 0으로 끝나야함
import sys

input = sys.stdin.readline
n = list(map(int, input().rstrip()))
n.sort(reverse=True)
if sum(n) % 3 == 0 and n[-1] == 0:
    print(''.join(list(map(str, n))))
else: print(-1)