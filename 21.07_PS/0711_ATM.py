x = input()
y = list(map(int, input().split()))
y = sorted(y)
rst = y[0]
for i in range(1, len(y)):
    rst += sum(y[:i+1])
print(rst)
