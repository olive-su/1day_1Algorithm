from sys import stdin

def min_position(arr, min):
    rst = 0
    for i in range(len(arr)):
        rst += abs(arr[i] - arr[min])
    return rst

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
min_idx = N//2
min_value = min_position(arr, min_idx)

while True:
    if min_idx == 0 or min_idx == N-1:
        break
    # min_idx보다 좌측에 위치한 집
    if min_position(arr, min_idx-1) <= min_value:
        min_value = min_position(arr, min_idx-1)
        min_idx -= 1
    # min_idx보다 우측에 위치한 집
    elif min_position(arr, min_idx+1) < min_value:
        min_value = min_position(arr, min_idx+1)
        min_idx += 1
    # 현재 위치가 최소 위치일 때
    else:
        break
print(arr[min_idx])
