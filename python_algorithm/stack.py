stack = []
num = int(input())
for _ in range(num):
  length = len(stack)
  command = input()
  if command[-1] == 'e':
    print(length)
  elif command[-1] == 'y':
    if length : print(0)
    else: print(1)
  elif command[0] == 't':
    if length: print(stack[-1])
    else: print(-1)
  elif command[-1] == 'p':
    if length: print(stack.pop())
    else: print(-1)
  else:
    stack.append(command[5:])

