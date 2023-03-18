# boj. 2792
# time: 16'

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
jewelry = []
for _ in range(m):
    jewelry.append(int(input()))

jewelry.sort()

def bin_search():
    answer = 0
    start, end = 1, jewelry[-1]
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for j in jewelry:
            cnt += j // mid
            if j % mid: cnt += 1
        
        if cnt > n:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
    
    return answer

print(bin_search())

