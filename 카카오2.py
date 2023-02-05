def solution(alp, cop, problems):
    time = 0
    search_min_v = 301
    search_max_v = 0
    # 최소 배열 찾기
    for i in problems:
        if i[0] + i[1] < 0:
            search_min_v = i[0] + i[1]
            min_pro = i
        if i[0] + i[1] > search_max_v:
            search_max_v = i[0] + i[1]
            max_pro = i
    
    # 최소치에 못미칠 경우
    if min_pro[0] < alp:
        time += min_pro[0] - alp
        alp = min_pro[0]
    if min_pro[1] < cop:
        time += min_pro[1] - cop
        alp = min_pro[1]
    

        




    answer = 0
    return answer