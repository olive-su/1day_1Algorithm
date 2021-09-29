def solution(answers):
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == student[0][(i + 1) % 5 - 1]: answer[0] += 1
        if answers[i] == student[1][(i + 1) % 8 - 1]: answer[1] += 1
        if answers[i] == student[2][(i + 1) % 10 - 1]: answer[2] += 1
    answery = []
    for i in range(3):
        if answer[i] == max(answer):
            answery.append(i + 1)
    return answery
