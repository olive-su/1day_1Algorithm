def staircase(n):
    case = [1]
    for i in range(1, n + 1):
        # case[0], case[1]은 1로 설정
        if i < 2:
            case.append(1) 
        else:
            case.append(case[i - 1] + case[i - 2])
    return case[n]
    
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
