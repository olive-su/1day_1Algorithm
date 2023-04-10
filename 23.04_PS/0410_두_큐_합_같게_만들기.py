# programmers. Level2 118667
# time: 32'

from collections import deque

def solution(queue1, queue2):
    answer = 0
    origin_q1, origin_q2 = queue1[:], queue2[:]
    queue1, queue2 = deque(queue1), deque(queue2)
    mid = (sum(queue1) + sum(queue2)) / 2
    if mid % 1: return -1
    
    mid = int(mid)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    
    while True:
        if q1_sum == mid:
            break
        if queue1 == origin_q1 or queue1 == origin_q2 or not queue1 or not queue2: 
            answer = -1
            break
        if answer > len(origin_q1) * 3:
            answer = -1
            break
        if q1_sum > q2_sum:
            t = queue1.popleft()
            queue2.append(t)
            q1_sum -= t
            q2_sum += t
        else:
            t = queue2.popleft()
            queue1.append(t)
            q2_sum -= t
            q1_sum += t
        answer += 1
    
    return answer