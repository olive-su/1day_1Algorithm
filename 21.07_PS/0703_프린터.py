def solution(priorities, location):
    answer = 0
    priorities_list = []
    for idx, i in enumerate(priorities):
        priorities_list.append((i, idx)) # 초기 인덱스 값과 원소 값 함께 저장
    while priorities_list:
        if priorities_list[0][0] != max(priorities_list)[0]: 
            # 대기목록 첫 번째 원소가 최댓값이 아니면 다시 리스트 맨 끝에 추가
            priorities_list.append(priorities_list[0])
        else:
            answer += 1
            if priorities_list[0][1] == location: 
                # location 문서가 출력되는 경우 반복문 종료
                break
        priorities_list.pop(0)
        
    return answer
