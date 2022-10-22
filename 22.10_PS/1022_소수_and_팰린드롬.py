# boj. 1747

import sys

def is_palindrome(num):
    length = len(str(num))
    div_num = pow(10, length - 1)
    for _ in range(length // 2):
        a = num // div_num
        b = num % 10
    
        if (a != b):
            return False
        num = (num % div_num) // 10
        div_num //= 100
    return True


input = sys.stdin.readline

INF = int(1e7) 
n = int(input())
flag = False # 수의 범위가 n을 넘었는지 체크

arr = [True] * (INF + 1)
arr[0], arr[1] = False, False

# 에라토스테네스의 체
for i in range(2, 1000 + 1):
    if arr[i] == True:
        num = 2
        while i * num <= INF:
            arr[i * num] = False
            num += 1
    
for i in range(n, INF + 1):
    if arr[i] == True and is_palindrome(i):
        sys.exit(print(i))

