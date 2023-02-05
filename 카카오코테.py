
from collections import deque
import copy

origin_q1, origin_q2 = [], []
rst = -1

def dfs(queue1, queue2, sum1, sum2, cnt):
    print
    global origin_q1, origin_q2, rst
    

    print(cnt)
    if rst != -1: return rst
    if queue1 == origin_q1 and queue2 == origin_q2: return -1
    if queue2 == origin_q1 and queue1 == origin_q2: return -1
    if len(queue1) == 0 or len(queue2) == 0: return -1
    if sum1 == sum2: return cnt
    dqueue1 = deque(queue1)
    dqueue2 = deque(queue2)
    val_pop1, val_pop2 = dqueue1.popleft(), dqueue2.popleft()

    nq1 = copy.deepcopy(queue1)
    nq1.append(val_pop2)
    nq2 = copy.deepcopy(queue2)
    nq2.append(val_pop1)
    rst = max(rst, dfs(nq1, dqueue2, sum1 + val_pop2, sum2 - val_pop2, cnt + 1))
    rst = max(rst, dfs(nq2, dqueue1, sum1 - val_pop1, sum2 + val_pop1, cnt + 1))



def solution(queue1, queue2):
    global origin_q1, origin_q2, rst
    origin_q1, origin_q2 = queue1, queue2
    cnt = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    total =  sum1 + sum2
    if total % 2: return -1 # 홀수일 경우 리턴
    
    dqueue1 = deque(queue1)
    dqueue2 = deque(queue2)
    val_pop1, val_pop2 = dqueue1.popleft(), dqueue2.popleft()

    nq1 = copy.deepcopy(queue1)
    nq1.append(val_pop2)
    nq2 = copy.deepcopy(queue2)
    nq2.append(val_pop1)
    rst = max(rst, dfs(nq1, dqueue2, sum1 + val_pop2, sum2 - val_pop2, cnt + 1))
    rst = max(rst, dfs(nq2, dqueue1, sum1 - val_pop1, sum2 + val_pop1, cnt + 1))

    return rst

if __name__ == "__main__":
    print(solution([3,2,7,2], [4,6,5,1]))