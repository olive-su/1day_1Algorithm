def binary_search(element, some_list):
    i = len(some_list) // 2
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
        elif element < some_list[i]:
            i = i // 2
        else:
            i = (len(some_list) - 1 - i) + (i // 2)
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
