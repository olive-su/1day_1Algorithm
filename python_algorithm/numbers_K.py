def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sorting_array = sorted(array[commands[i][0]-1 : commands[i][1]])
        answer.append(sorting_array[commands[i][2]-1])
        
    return answer
