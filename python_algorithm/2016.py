def solution(a, b):
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month_fin = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = b
    for i in range(a - 1): # 인덱스 범위만큼 반복문 수행해야 하므로 '-1' 해줌
        days += month_fin[i]
    return week[days % 7]
