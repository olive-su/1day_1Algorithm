# boj. 11816
# time : 15'

def hex_to_dec(x):
    rst, num = 0, 0
    n = x[2:]
    while n:
        s = n[-1]
        if s >= 'a': s = ord(s) - ord('a') + 10
        else: s = int(s)
        rst += (16 ** num) * s
        num += 1
        n = n[:-1]
    return rst

def oct_to_dec(x):
    rst, num = 0, 0
    n = x[1:]
    while n:
        s = n[-1]
        rst += (8 ** num) * int(s)
        num += 1
        n = n[:-1]
    return rst

x = input().rstrip()
if '0x' in x:
    x = hex_to_dec(x)
elif '0' == x[0]:
    x = oct_to_dec(x)

print(x)
