# programmers

def solution(s):
    answer = []
    s = s[1:-2].replace('{', '')
    s = s.split('},')
    s.sort(key = lambda x : len(x))
    
    for i in s:
        arr = i.split(',')
        for a in arr:
            if a not in answer:
                answer.append(a)

    answer = list(map(int, answer))
    
    return answer
