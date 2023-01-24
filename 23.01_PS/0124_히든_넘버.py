# boj. 8595
# time : 7'

length = int(input())
n = input().rstrip()
rst, s = 0, ''
for i in range(length):
    if n[i].isdigit(): s += n[i]
    elif s: 
        rst += int(s)
        s = ''

print(rst + int(s)) if s else print(rst)
