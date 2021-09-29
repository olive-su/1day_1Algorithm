def solution(numbers):
    answer = []
    flag = 1
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            for k in range(len(answer)):
                if(answer[k] == numbers[i] + numbers[j]):
                    flag = 0
                    break
                flag = 1
            if (flag == 1):
                answer.append(numbers[i] + numbers[j])
    answer.sort()      
    return answer
