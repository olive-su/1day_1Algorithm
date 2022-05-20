import sys

input = sys.stdin.readline
n, l = map(int, input().split())

i, cnt = 1, 0 
while True:
    if str(l) not in str(i):
        cnt += 1
    if cnt == n: break
    i += 1

print(i)
