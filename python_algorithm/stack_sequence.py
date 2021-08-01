import sys

a = int(sys.stdin.readline())
b, stack, answer = [], [], []
for _ in range(a):
    b.append(int(sys.stdin.readline()))
i = 1
while b:
    if stack and stack[-1] == b[0]:
        answer.append('-')
        stack.pop()
        b.pop(0)
    else:
        if i > a: break
        answer.append('+')
        stack.append(i)
        i += 1
if stack: print('NO')
else: print('\n'.join(answer))
