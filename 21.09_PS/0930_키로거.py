from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    string = stdin.readline().rstrip()
    stack, temp = [], []
    for s in string:
        if s == '<':
            if stack:
                temp.append(stack.pop())
        elif s == '>':
            if temp:
                stack.append(temp.pop())
        elif s == '-':
            if stack:
                stack.pop()
        else:
            stack.append(s)
    if temp:
        temp.reverse()
    print(''.join(stack+temp))
