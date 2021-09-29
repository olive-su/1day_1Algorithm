def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    pop_num = 0
    while progresses != []:
        if progresses[-1] >= 100: # 작업 진도가 100을 넘을 경우 배포
            pop_num += 1
            progresses.pop()
        elif pop_num: # 배포할 작업이 있을 경우 누적된 작업 한꺼번에 배포
            answer.append(pop_num)
            pop_num = 0
        else : # 각 작업의 진도대로 더해서 스택에 추가
            s_stack = map(lambda x, y : x + y, progresses, speeds)
            progresses = list(s_stack)
    answer.append(pop_num)
    
    return answer
