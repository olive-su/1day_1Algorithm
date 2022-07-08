# programmers

'''
출차 내역 x : 23:59
단위 시간 올림
같은 날 두번 이상 방문
'''
from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    basic_t, basic_f, unit_t, unit_f = fees
    car_dict = defaultdict(list)
    
    for r in records:
        time, num, sign = r.split()
        car_dict[num].append(time)
        
    for key, value in car_dict.items():
        if len(value) % 2: # 출차 기록 x
            car_dict[key].append("23:59")
    
    cars = list(car_dict.items())
    cars.sort(key = lambda x : x[0]) # 차 번호 정렬
        
    for i, j in cars:
        in_time = -1
        total = 0
        for k in j:
            hh, mm = k.split(':')
            time = int(hh) * 60 + int(mm)
            if in_time == -1: in_time = time
            else:
                total += time - in_time
                in_time = -1
        total -= basic_t
        if total > 0:
            total = ceil(total / unit_t) * unit_f
        else:
            total = 0
        answer.append(total + basic_f)
    
    return answer
