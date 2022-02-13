from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

flag = 0  # 고정점 유무
start, end = 0, n - 1
while start <= end:
    mid = (start + end) // 2
    if mid == arr[mid]:
        flag = 1
        print(mid)
        break
    # 현재 리스트의 숫자가 인덱스 보다 작으므로 이전 범위들에는 고정점이 존재하지 않음
    elif arr[mid] < mid: 
        start = mid + 1
    else:
        end = mid - 1

if not flag: # 고정점이 존재하지 않으면 '-1' 출력
    print(-1)
