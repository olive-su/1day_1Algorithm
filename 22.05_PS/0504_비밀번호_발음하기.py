import sys

input = sys.stdin.readline
vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    command = input().rstrip()
    if command == 'end': break
    flag, now = 0, 0
    cnt_c, cnt_v = 0, 0
    if command[0] in vowels: now, flag, cnt_v = 1, 1, 1 
    else: cnt_c = 1
    for i in range(1, len(command)):
        if command[i] in vowels:
            if now: cnt_v += 1
            else:cnt_c, cnt_v = 0, 1
            flag, now = 1, 1
        else:
            if not now: cnt_c += 1
            else:cnt_c, cnt_v = 1, 0
            now = 0
        if command[i - 1] == command[i]:
            if command[i] != 'o' and command[i] != 'e':
                flag = 0
                break
        if cnt_c == 3 or cnt_v == 3:
            flag = 0
            break
    if not flag: print(f'<{command}> is not acceptable.')
    else: print(f'<{command}> is acceptable.')
