import sys

x = ''
while True:
    stack = []
    sig = 0
    x = sys.stdin.readline()
    if x == '.\n': break
    for i in x:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack.pop() != '(':
                sig = 1
                break
        elif i == ']':
            if not stack or stack.pop() != '[':
                sig = 1
                break
    if stack or sig: print("no")
    else: print("yes")
