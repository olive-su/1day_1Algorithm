# programmers
# time: 40'

answer = ''

def balance(c):
    global answer
    
    if c == '': # 빈 문자열일 경우
        return 
    string = c[0]
    cnt = [0, 0] # '('개수, ')'개수
    
    if string == ')': # ')' 맨처음 등장
        cnt[1] += 1
        flag = False # 균형 문자열 여부
    else:
        cnt[0] += 1
        flag = True
    
    for i in range(1, len(c)):
        if cnt[0] == cnt[1]: # 균형 문자열
            if flag: # 올바른 문자열
                answer += string
                return balance(c[i:])
            else:
                answer += '('
                balance(c[i:]) # 뒤 문자열 u 처리
                answer += ')'
                for s in range(1, len(string) - 1):
                    if string[s] == '(': answer += ')'
                    else: answer += '(' 
                return
        else:
            string += c[i]
            if c[i] == '(': cnt[0] += 1
            else: cnt[1] += 1
            if cnt[0] < cnt[1]: flag = False
            
    # 남은 균형 문자열 처리        
    if cnt[0] == cnt[1]: # 균형 문자열
        if flag: # 올바른 문자열
            answer += string
        else:
            answer += '('
            answer += ')'
            for s in range(1, len(string) - 1):
                if string[s] == '(': answer += ')'
                else: answer += '('
    

def solution(p):
    global answer

    balance(p)
    
    return answer