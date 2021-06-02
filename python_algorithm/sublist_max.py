def sublist_max(profits):
    max_profit = profits[0]
    for i in range(len(profits) + 1):
        for j in range(len(profits) + 1):
            if max_profit < sum(profits[i:j]):
                max_profit = sum(profits[i:j])
    return max_profit

print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
