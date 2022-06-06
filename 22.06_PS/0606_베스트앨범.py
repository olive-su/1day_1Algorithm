# 프로그래머스 해시
# time : 19'

'''
장르 -> 노래 -> 고유 번호
'''

from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    g_dict, p_dict = defaultdict(int), defaultdict(list)
    for i in range(len(genres)):
        g_dict[genres[i]] += plays[i]
        p_dict[genres[i]].append((i, plays[i]))
    
    sort_g = sorted(g_dict.items(), key=lambda x : x[1], reverse=True)
    
    for genre, total in sort_g:
        sort_p = sorted(p_dict[genre])
        sort_p = sorted(sort_p, key=lambda x : x[1], reverse=True)
        
        for r in range(len(sort_p)):
            if r > 1: break
            answer.append(sort_p[r][0])
    
    return answer