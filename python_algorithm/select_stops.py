def select_stops(water_stops, capacity):
    stops_root = []
    # for문의 시작점이 [1]이므로 처음에 [0]인덱스를 빼줌 
    water = capacity - water_stops[0]
    for i in range(1, len(water_stops)):
        distance = water_stops[i] - water_stops[i-1]
        # 현재 용량으로 다음 약수터를 갈 수 없으면
        # 이전 인덱스를 최종 리스트에 추가해줌
        if water < distance:
            stops_root.append(water_stops[i-1])
            water = capacity - distance
        else:
            water -= distance
    stops_root.append(water_stops[len(water_stops)-1])
    return stops_root


list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
