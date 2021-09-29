import heapq

def solution(scoville, K):
    num = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        num += 1
    
    return num
