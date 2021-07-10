def solution(s):
    answer = ''
    std = ''
    dic = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(s)):
        if str(s[i]).isdigit():
            answer += str(s[i])
        else:
            std+=s[i]
            if std in dic:
                answer += str(dic.index(std))
                std = ''
    
    return int(answer)
