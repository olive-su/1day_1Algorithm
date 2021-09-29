def find_same_number(some_list, start = 1, end = None):
    if end == None:
        end = len(some_list) - 1

    if start == end:
        return start

    mid = (start + end) // 2

    # 좌측 숫자 개수 카운트(오른쪽 = 전체 - 왼쪽)
    left_count = 0

    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1

    # 양쪽 중 과반 이상의 숫자가 있는 범위 내에서 탐색 재진행
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)

    return find_same_number(some_list, mid + 1, end)

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
