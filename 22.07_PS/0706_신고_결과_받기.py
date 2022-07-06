# programmers
# time : 15'

from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    report_dict = defaultdict(int) # 신고 횟수
    id_dict = defaultdict(list) # 신고한 사람

    for i in range(len(report)):
        a, b = report[i].split()
        if b not in id_dict[a]:
            id_dict[a].append(b)
            report_dict[b] += 1

    for i in id_list:
        num = 0
        for j in id_dict[i]:
            if report_dict[j] >= k:
                num += 1
        answer.append(num)

    return answer
