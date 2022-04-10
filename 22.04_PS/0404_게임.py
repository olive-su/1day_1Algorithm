import sys

input = sys.stdin.readline
x, y = map(int, input().split())
rst = -1

z = (100 * y) // x # int(y / x * 100) 5퍼 틀렸습니다.
start = 0
end = x
while start <= end:
    mid = (start + end) // 2
    val = 100 * (y + mid) // (x + mid)
    if val > z:
        rst = mid
        end = mid - 1
    else:
        start = mid + 1
print(rst)