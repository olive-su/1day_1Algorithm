def solution(people, limit):
    answer, start, end = 0, 0, len(people) - 1
    people.sort()
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer + 1 if start == end else answer

'''
pop 으로 했을 경우 효율성 테스트 1 불통

def solution(people, limit):
    answer = 0
    people.sort()
    while len(people) > 1:
        if people[-1] <= limit // 2:
            answer += len(people) // 2
            break
        if people[0] + people.pop() <= limit:
            people.pop(0)
        answer += 1
    return answer + 1 if len(people) % 2 else answer
'''
