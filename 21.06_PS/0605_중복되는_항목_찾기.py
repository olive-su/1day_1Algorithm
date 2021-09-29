def find_same_number(some_list):
    # 중복된 요소 리스트에서 제거
    for i in range(1, len(some_list)):
        some_list.remove(i)
    return some_list[0]
    
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
