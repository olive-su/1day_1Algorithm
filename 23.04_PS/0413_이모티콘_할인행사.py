# time: 40'
# 이모티콘 플러스 가입, 판매액
# return 이모티콘 플러스 가입 수, 매출액

from itertools import product

def purchase_emoticons(discount, new_discount, new_price):
    rst = 0
    for i in range(len(new_discount)):
        if new_discount[i] >= discount:
            rst += new_price[i]
    
    return int(rst)

def solution(users, emoticons):
    answer = [0, 0]
    discount_rate = [0.1, 0.2, 0.3, 0.4]
    prod =  product(discount_rate, repeat=len(emoticons))
    for p in prod:
        tmp = [0, 0]
        new_discount = list(zip(p, emoticons))
        new_price = list(map(lambda x : (1-x[0]) * x[1], new_discount))
        for discount, price_lim in users:
            money = purchase_emoticons(discount / 100, p, new_price)
            if money >= price_lim: tmp[0] += 1
            else: tmp[1] += money
        if tmp[0] > answer[0] or (tmp[0] == answer[0] and tmp[1] > answer[1]):
            answer = tmp[:]
            
    return answer