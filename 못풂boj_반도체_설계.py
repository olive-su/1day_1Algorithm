import sys

# input = sys.stdin.readline
# n = int(input())
# dp = [1e9] * (n + 1)

# for i in range(1, n + 1):
#     for j in range()


arr = [6, 2, 5, 1, 7, 4, 8, 3]

k = 0
n = 8

length = [1] * (n + 1)

for k in range(1, n):
    for i in range(k):
        if(arr[i] < arr[k]):
            length[k] = max(length[k], length[i] + 1)
    
print(length)


