from collections import deque
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    p = stdin.readline().rstrip()
    n = stdin.readline().rstrip()
    int_arr = stdin.readline().lstrip('[').rstrip(']\n').split(',')
    int_arr = deque(int_arr)
    order = 1
    flag = 0
    for i in p:
        if i == 'R':
            order *= -1
        else:
            if n == '0' or len(int_arr) == 0:
                flag = 1
                break
            if order > 0:
                int_arr.popleft()
            else:
                int_arr.pop()
    if flag:
        print('error')
    else:
        int_arr = list(int_arr)
        if order < 0:
            int_arr.reverse()
        print('[', end='')
        for i in int_arr[:-1]:
            print(i, end=',')
        if int_arr:
            print(int_arr[-1],end='')
        print(']')
