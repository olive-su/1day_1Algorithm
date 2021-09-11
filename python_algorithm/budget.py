from sys import stdin
N = int(stdin.readline())
request = list(map(int, stdin.readline().split()))
budget = int(stdin.readline())
request.sort()
rst = budget // N # 예산이 입력된 숫자보다 작은 경우 처리하기 위함
start = request[0]
end = request[-1]
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in request:
        if i < mid:
            total += i
        else:
            total += mid
    if total <= budget:
        rst = mid
        start = mid + 1
    else:
        end = mid - 1
print(rst)
