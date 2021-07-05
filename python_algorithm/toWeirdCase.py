def solution(s):
    s_len = 2
    answer = ''
    for i in s:
        if i == ' ':
            answer+=i
            s_len = 2
            continue
        elif s_len % 2 == 0: answer += i.upper()
        else: answer += i.lower()
        s_len += 1
    return answer
