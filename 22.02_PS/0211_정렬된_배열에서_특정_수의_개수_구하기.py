from sys import stdin
import bisect
n, x = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
rst = bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)
print(rst) if rst else print(-1) # 값이 x인 원소가 하나도 없는 경우
