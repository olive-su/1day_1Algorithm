from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
rst = 10000000000
start, end = 0, n-1
optimal_val = (arr[0], arr[-1])
while start < end:
    now = abs(arr[start] + arr[end])  # 혼합 용액의 특성 값을 저장
    if now < rst:  # 혼합 용액의 특성 값이 최소 값이 등장할 경우, 최소 값을 갱신한다.
        rst = now
        optimal_val = (arr[start], arr[end])

    # 절대값이 더 큰 값의 pin을 안쪽으로 더 좁힌다.
    if abs(arr[start]) < abs(arr[end]):
        end -= 1
    else:
        start += 1
print(optimal_val[0], optimal_val[1])

