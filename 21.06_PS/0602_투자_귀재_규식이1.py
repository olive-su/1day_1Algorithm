def sublist_max(profits):
    # 초기값 설정을 위해 임의로 인덱스 0의 값을 할당함
    max_profit = profits[0]
    # 최대 범위 인덱스 값 증가
    for i in range(len(profits) + 1):
        # 최소 범위 인덱스 값 증가
        for j in range(len(profits) + 1):
            if max_profit < sum(profits[i:j]):
                max_profit = sum(profits[i:j])
    return max_profit

print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
