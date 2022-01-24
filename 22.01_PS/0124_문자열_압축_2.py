def solution(s):
    rst = len(s)
    answer = len(s)
    flag = 1
    # 최대 압축 길이 = '문자열 길이 / 2'
    length = len(s) // 2
    for l in range(length, 0, -1): # 최대 압축 길이부터 1까지 줄여나감
        string = ''
        i = 0
        answer = len(s)
        while i <= len(s):
            if string == s[i:i+l]: # 이전 문자열과 동일할 경우 압축 가능
                answer -= l
                flag += 1
            else:
                if flag > 1:
                    answer += len(str(flag))
                string = s[i:i+l]
                flag = 1
            i += l
        rst = min(rst, answer)
    
    return rst
