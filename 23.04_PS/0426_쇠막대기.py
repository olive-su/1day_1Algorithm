# boj. 10799

pieces = list(input())
stack = []
cnt = 0
stack.append(pieces[0])

for i in range(1, len(pieces)):
    if pieces[i] == '(':
        stack.append('(')
    else:
        if pieces[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            cnt += 1
            stack.pop()

print(cnt)
