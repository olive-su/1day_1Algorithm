def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if not signs[i]: absolutes[i] *= (-1)
    return sum(absolutes)
