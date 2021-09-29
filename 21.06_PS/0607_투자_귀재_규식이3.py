def sublist_max(profits):
    max_profit_so_far = profits[0]
    max_check = max(profits[0]+profits[1], profits[1])
    for i in range(2, len(profits)):
        max_profit_so_far = max(max_profit_so_far, max_check)
        max_check = max(max_check + profits[i], profits[i])
    max_profit_so_far = max(max_profit_so_far, max_check)
    return max_profit_so_far
    
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
