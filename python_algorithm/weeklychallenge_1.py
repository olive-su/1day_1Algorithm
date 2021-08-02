def solution(price, money, count):
    fee = 0
    for i in range(count):
        fee += price * (i+1)
    fee -= money 
    return fee if fee > 0 else 0
