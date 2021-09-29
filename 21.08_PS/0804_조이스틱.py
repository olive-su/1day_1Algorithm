def solution(name):
    answer = 0
    name = list(name)
    if name[1] == 'A':
        name.append(name.pop(0))
        name.reverse()
        answer -= 1
    for i in range(len(name)):
        if i > 0 and name[i-1] == 'A' and name[i] == 'A': continue
        if ord(name[i]) < ord('N'):
            answer += (ord(name[i]) - ord('A'))
        else:
            answer += abs(ord(name[i]) - ord('Z')) + 1
        answer+=1
    return answer - 1
