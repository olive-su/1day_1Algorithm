N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, N+1):
        if mid//i < N: cnt += mid//i
        else: cnt += N
    
    if cnt >= K: 
        rst = mid
        end = mid - 1
    else:
        start = mid + 1
print(rst)
