import sys, collections
a, c = [], []
n = int(sys.stdin.readline())
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
# 산술평균
print(round(sum(a) / n))
# 중앙값
print(a[(n//2)])
# 최빈값
value = 0
counter = collections.Counter(a)
for i in a:
    if counter[i] > value:
        c = []
        c.append(i)
        value = counter[i]
    elif counter[i] == value and i not in c:
        c.append(i)
if len(c) > 1:print(c[1])
else: print(c[0])
# 범위
print(a[-1]-a[0])
