# programmers
from itertools import combinations

# 최소성 판단
def candidate(arr, col):
    rst = [[] for _ in range(len(arr))]

    for a in range(len(arr)):
        for c in col:
            rst[a].append(arr[a][c])
    rst = list(map(tuple, rst))
    rst = set(rst)
    
    if len(rst) == len(arr):
        return True
    else:
        return False
            

def solution(relation):
    answer = 0
    
    col_len = len(relation[0])
    col_check = [i for i in range(col_len)]
    col_valid = []
    for i in range(1, col_len + 1):
        comb = list(combinations(col_check, i))

        for c in comb:
            stop = 0
            for v in col_valid:
                flag = 0
                for j in v:
                    if j in c:
                        flag += 1
                if len(v) == flag: 
                    stop = 1
                    break

            if stop:
                continue
                
            if candidate(relation, c):
                col_valid.append(c)
                answer += 1
                    
    return answer