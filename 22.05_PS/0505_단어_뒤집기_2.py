import sys

input = sys.stdin.readline
s = input().rstrip()
rst, stack = [], []
flag, sig = 0, 0
for i in s:
    if i == '<':
        if len(stack) > 0:
            rst.append(''.join(reversed(stack)))
            stack = []
        stack.append(i) 
        flag = 1
    elif i == '>':
        stack.append(i)
        rst.append(''.join(stack))
        stack = []
        flag = 0
    else:
        if flag:
            stack.append(i) 
            continue # 태그 구간
        else:
            if i == ' ' and len(stack) > 0:
                rst.append(''.join(reversed(stack)))
                stack = []
            else:
                stack.append(i)
if len(stack) > 0:
    rst.append(''.join(reversed(stack)))
for i in range(len(rst)):
    if rst[i][0] == '<' or i == len(rst) - 1:
        print(rst[i], end='')
    elif rst[i + 1][0] == '<':
        print(rst[i], end='')
    else:
        print(rst[i], end=' ')