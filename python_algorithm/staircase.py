def calc(n):
    if n <= 1:
        return 1
    else:
        return n // 2 + calc(n - 1)

def staircase(n):
    case = 1
    case += calc(n)
    return case
        
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))

