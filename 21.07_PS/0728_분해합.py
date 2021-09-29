import sys

num = int(sys.stdin.readline().rstrip())
for i in range(num):
    str_i = list(map(int, str(i)))
    if sum(str_i) + i == num:
        print(i)
        sys.exit(0)
print(0)
