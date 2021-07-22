t = list(map(int, input().split()))
m = (t[0]*60 + t[1])-45
if m < 0: m = 1440 + m
print('{} {}'.format(m//60, m%60) )
