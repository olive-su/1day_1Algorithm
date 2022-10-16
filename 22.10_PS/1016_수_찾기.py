# boj. 1920

import sys

input = sys.stdin.readline
n = int(input())
compare_arr = list(map(int, input().split()))
compare_arr.sort()

m = int(input())
target_arr = list(map(int, input().split())) 

def binary_search(target):
    start, end = 0, n - 1

    while start <= end:
        mid = (end + start) // 2
        if compare_arr[mid] == target:
            return 1
        elif target < compare_arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for t in target_arr:
    print(binary_search(t))

