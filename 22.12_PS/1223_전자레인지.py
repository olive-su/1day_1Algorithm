import sys

# time : 7'
# 300' 60' 10"
input = sys.stdin.readline
t = int(input())
a, b, c = [0] * 3
 
if t // 300:
    a = t // 300
    t %= 300
if t // 60:
    b = t // 60
    t %= 60
if t // 10:
    c = t // 10
    t %= 10
if t: print(-1)
else: print(a, b, c, sep=' ') 
