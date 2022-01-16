from sys import stdin

S = list(map(int, stdin.readline().rstrip()))
rst = S[0]

for i in range(1, len(S)):
    if S[i] == 0 or S[i-1] == 0:
        rst += S[i]
    else:
        rst *= S[i]

print(rst)
