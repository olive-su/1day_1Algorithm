from sys import stdin
L = int(stdin.readline())
string = stdin.readline().rstrip()
rst = 0
for i in range(L):
    rst += (ord(string[i]) - ord('a') + 1) * (31**i)
print(rst % 1234567891)
