import sys
import bisect

input = sys.stdin.readline
n, m = map(int, input().split())

dot = list(map(int, input().split()))
dot.sort()
for _ in range(m):
    start, end = map(int, input().split())
    print(bisect.bisect_right(dot, end) - bisect.bisect_left(dot, start))
