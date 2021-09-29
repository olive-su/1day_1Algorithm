# 퀵 정렬 1단계 : 두 함수를 바꿔주는 swap 함수 구현
def swap_elements(my_list, index1, index2):
    tmp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = tmp
    return my_list
