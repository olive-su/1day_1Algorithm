def swap_elements(my_list, index1, index2):
    tmp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = tmp
    return my_list


def partition(my_list, start, end):
  
    b = 0 
    i = 0 
    p = end # pivot

    for i in range(0, p):
        if my_list[p] < my_list[i]:
            continue
        else:
            swap_elements(my_list, b, i)
            b += 1
            i += 1

    swap_elements(my_list, b, p)
    return b


# 퀵 정렬
def quicksort(my_list, start, end):
    merge_index = 0
    merge_index = partition(my_list,start,end)

    if merge_index == start:
        return my_list

    quicksort(my_list,0,merge_index-1 ) # 왼쪽 quicksort
    quicksort(my_list,merge_index,end) # 오른쪽 quicksort
