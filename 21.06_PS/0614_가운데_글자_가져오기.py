def solution(s):
    answer = ""
    middle_idx = len(s) // 2
    answer = s[middle_idx]
    if len(s) % 2 == 0:
        answer = s[middle_idx - 1] + answer
        
    return answer
