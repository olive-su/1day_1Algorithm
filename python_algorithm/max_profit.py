def max_profit(stock_list):
    profit = stock_list[1] - stock_list[0]
    for i in range(len(stock_list)-2):
        # i 인덱스 뒤에 있는 값들을 내림차순으로 정렬한 뒤 최댓값 추출
        sorting_list = sorted(stock_list[i + 1 : len(stock_list)-1], reverse = True)
        # max로 수익 최대값 갱신
        profit = max(profit, sorting_list[0] - stock_list[i])
    return profit

print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
