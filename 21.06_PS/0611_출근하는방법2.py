#높이 n개의 계단을 올라가는 방법을 리턴
def staircase(stairs, possible_steps):
    result = 0
    # 계단 개수가 0 또는 1인 경우, 올라가는 방법 : 1
    if stairs < 2:
        return 1
    # n번 계단 전까지의 부분 문제 해결을 위해 for문 수행
    for i in range(len(possible_steps)):
        if (stairs >= possible_steps[i]):
            result += staircase(stairs-possible_steps[i], possible_steps)
    return result
       
print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
