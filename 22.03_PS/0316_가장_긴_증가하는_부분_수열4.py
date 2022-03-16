import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
d[0] = 1
for a in range(1, n):
    max_v = 0
    for i in range(a):
        if arr[a] > arr[i]:
            max_v = max(max_v, d[i])
    if max_v == 0:
        d[a] = 1
    else:
        d[a] = max_v + 1

before = max(d)
print(before)
p_arr = []

for i in range(n-1, -1, -1):
    if d[i] == before:
        p_arr.append(arr[i])
        before -= 1

p_arr.reverse()
[print(i, end=' ') for i in p_arr]
