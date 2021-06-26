def solution(lottos, win_nums):
    answer = [0, 0]
    for num in lottos:
        if num == 0:
            answer[0] += 1
        elif num in win_nums:
            answer[0] += 1
            answer[1] += 1
    for i in range(2):
        if answer[i] < 2 : answer[i] = 1
        answer[i] = 7 - answer[i]
    return answer
