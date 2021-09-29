def solution(n, times):
    start = 1
    end = max(times) * n
    
    while start < end:
        mid = (start + end) // 2
        cnt = 0
        
        for i in times:
            cnt += mid // i
            
        if cnt < n:
            start = mid + 1
        else:
            end = mid
    return start
