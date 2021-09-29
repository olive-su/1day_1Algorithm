def solution(s):
    answer = len(s)
    for split in range(1, (len(s) // 2) + 1): # '최대 압축 길이' = '문자열 길이' / 2
        s_list = []
        i = 0
        while i + split <= len(s):
            # 앞의 문자열이 연속적으로 나타날 경우
            if len(s_list) > 0 and s_list[-1] == s[i:i+split]:
                s_list.pop()
                # 문자열 연속이 처음 나타난 경우 문자열 앞에 '2'를 삽입
                if len(s_list) == 0 or str(s_list[-1]).isalpha():
                    s_list.append(2)
                # 문자열 연속이 처음이 아니므로 연속 횟수에 1을 더함
                else:
                    s_list[-1] += 1
            s_list.append(s[i:i+split])
            i += split
        # 일정 개수 단위로 잘라서 압축한 이후, 문자열이 남았을 경우 남은 문자열을 모두 덧붙임
        s_list.append(s[i:])
        s_str = ''.join(map(str,s_list))
        # 문자열 길이의 최소값 갱신
        answer = min(answer, len(s_str))
        
    return answer
