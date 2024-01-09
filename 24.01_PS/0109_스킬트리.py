def solution(skill, skill_trees):
    answer = 0

    for now in skill_trees:
        target = ''  # taget 문자열 초기화
        for n in now:
            if n in skill:
                target += n  # skill에 포함된 문자열만 남김
        if target == skill[:len(target)]:  # skill 문자열이 순서를 지켰는 지 확인
            answer += 1

    return answer
