n = int(input())
step = [0, ]
for i in range(n):
    step.append(int(input()))
d = [0] * (n + 1)
if n == 1:
    print(step[1])
else:
    d[0] = 0
    d[1] = step[1]
    d[2] = max(step[1] + step[2], step[2])
    for j in range(3, n + 1):
        d[j] = max((d[j - 2] + step[j]), (d[j - 3] + step[j-1] + step[j]))
    print(d[n])
