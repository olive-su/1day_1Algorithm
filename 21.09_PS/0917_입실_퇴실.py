def solution(enter, leave):
    stack = []
    answer = {}
    for i in range(1, len(enter) + 1):
        answer[i] = 0
    while leave:
        if leave[0] in stack:
            stack.remove(leave[0])
            answer[leave.pop(0)] += len(stack)
            for i in stack:
                answer[i] += 1
        else:
            stack.append(enter.pop(0))
    rst = list(answer.values())
    return rst
