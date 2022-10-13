# boj. 2023

import sys
import math

input = sys.stdin.readline
n = int(input())

start = int(math.pow(10, n - 1))
end = int(math.pow(10, n))

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

for i in range(start, end):
    first_num = i // start 
    if first_num == 2 or first_num == 3 or first_num == 5 or first_num == 7: 
        flag = False
        div = start // 10
        
        while div > 0:
            target = i // div
            if not is_prime(target):
                flag = True
                break
            div //= 10

        if flag: continue
        print(i)

