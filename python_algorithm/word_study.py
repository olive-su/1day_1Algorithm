import sys
m, n = [0, ''], sys.stdin.readline().rstrip().upper()
for i in set(n):
    cnt = n.count(i)
    if m[0] < cnt:
        m = [cnt, i]
    elif m[0] == cnt:
        m[1] = '?'
print(m[1])
