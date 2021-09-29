def solution(participant, completion):
    participant.sort() # participant = sorted(participant) 로 바꾸기
    completion.sort() # completion= sorted(completion) 로 바꾸기
    for i in range(len(participant) - 1):
        if completion[i] != participant[i]: # 반복문 수행 중 같지 않는 원소가 나오면 값 리턴
            return participant[i]
    return participant[-1] # 반복문이 끝까지 돌 동안 값이 나오지 않으면 맨 마지막 항목 리턴
