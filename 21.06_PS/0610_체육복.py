def solution(n, lost, reserve):
    answer = n - len(lost)
    # 이미 체육복을 빌려준 학생의 경우 '-1'로 처리
    # 도난당한 학생과 여분이 있는 학생이 동일할 경우
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if(lost[i] == reserve[j]):
                answer += 1
                lost[i] = -1 # 아래 for문의 중복 판정 방지 위함
                reserve[j] = -1
                break
    # 여분이 있는 학생이 도난당한 학생에게 체육복을 빌려줄 수 있는 경우
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if (abs(lost[i] - reserve[j]) == 1):
                answer += 1
                reserve[j] = -1
                break
    return answer
