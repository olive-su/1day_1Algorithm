# boj. 11004
# 퀵 정렬 - pypy
# 내장 함수로 sort() 시에는 시간초과 X

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))

def Quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[n / 2]
    start, end = 1, len(arr) - 1
    s_list, m_list, l_list = [], [], [] # small_list, middle_list, large_list

    while True:
        if start >= end:
            if start == end:    
                if arr[start] < pivot:
                    s_list.append(arr[start]) 
                elif arr[start] > pivot:
                    l_list.append(arr[start])
                else:
                    m_list.append(arr[start])
            break
        
        if arr[start] < pivot:
            s_list.append(arr[start]) 
        elif arr[start] > pivot:
            l_list.append(arr[start])
        else:
            m_list.append(arr[start])

        if arr[end] < pivot:
            s_list.append(arr[end]) 
        elif arr[end] > pivot:
            l_list.append(arr[end])
        else:
            m_list.append(arr[end])

        start += 1
        end -= 1
    
    return Quick_sort(s_list) + m_list + Quick_sort(l_list)

    
arr = Quick_sort(arr)
print(arr[k - 1])

