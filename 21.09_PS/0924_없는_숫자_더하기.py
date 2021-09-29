def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        num.remove(i)
    return sum(num)
