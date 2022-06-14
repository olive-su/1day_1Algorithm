import sys
from itertools import combinations

input = sys.stdin.readline
arr = list(map(int, input().split()))
while arr[0] != 0:
    n = arr.pop(0)

    com = list(combinations(arr, 6))
    for i in com:
        for j in i:
            print(j, end=' ')
        print()
    print()
    arr = list(map(int, input().split()))
