def sum_in_list(search_sum, sorted_list):
    for i in range(len(sorted_list) - 1):
        if search_sum - sorted_list[i] in sorted_list[i+1:]:
            return True
    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
