import sys

input = sys.stdin.readline
duck = ['q','u','a','c','k']
arr = []
cnt, rst  = 0, 0
sound = input().rstrip()

for i in sound:
    rst = max(rst, cnt)
    flag = 1
    for j in arr:
        if len(j) < 5 and i == duck[len(j)]:
            j.append(i)
            if len(j) == 5:
                cnt -= 1
            flag = 0
            break
    if flag:
        if i == 'q':
            arr.append(['q'])
            cnt += 1
        else:
            sys.exit(print(-1))
for i in arr:
    if len(i) != 5:
        sys.exit(print(-1))
print(rst)