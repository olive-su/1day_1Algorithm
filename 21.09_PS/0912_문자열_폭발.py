from sys import stdin
string = list(stdin.readline().rstrip())
bomb = list(stdin.readline().rstrip())
stack = []
for i in range(len(string)):
    stack.append(string[i])
    if stack[-(len(bomb)):] == bomb: # bomb와 같은 문자열 찾기 위함
        for j in range(len(bomb)):
            stack.pop()
print(''.join(stack)) if stack else print('FRULA')
