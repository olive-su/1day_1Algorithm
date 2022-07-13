# programmers
# 40'

'''
코스이름 저장 - 개수
정렬 이름 개수대로
'''

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    course_dict = defaultdict(int)
    answer = []
    v = [0] * (course[-1] + 1)

    for o in orders:
        o = list(o)
        for i in course:
            comb = list(map(sorted, combinations(o, i)))

            for c in comb:
                course_dict[''.join(c)] += 1

    course_items = list(course_dict.items())

    course_items.sort(key=lambda x : x[1], reverse=True)

    for target, cnt in course_items:
        if cnt < 2:
            break
        if v[len(target)] == 0:
            v[len(target)] = cnt # 개수 최댓값
        if v[len(target)] == cnt:
            answer.append(target)

    return sorted(answer)

