import sys
limit_num = int(list(sys.stdin.readline().split())[1])
a = list(sys.stdin.readline().split())
a = list(map(int, a))
max_value = 0
for i in range(len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a)):
            value = a[i] + a[j] + a[k]
            if value <= limit_num:
                max_value = max(value, max_value)
print(max_value)
