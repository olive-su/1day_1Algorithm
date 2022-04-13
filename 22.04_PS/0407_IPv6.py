import sys

input = sys.stdin.readline
address = input().rstrip()
origin = [[] for _ in range(8)]
sep_cnt = address.count(':')
idx = 0

for i in range(len(address)):
    if address[i] == ':':
        if i > 0 and address[i - 1] == ':': # 연속 ':' 등장 시
            while idx + sep_cnt < 8:
                origin[idx] = ['0', '0', '0', '0'] # 앞을 '0'으로 채워줌
                idx += 1
        else:
            while len(origin[idx]) < 4:
                origin[idx].insert(0, '0') # 앞을 '0'으로 채워줌
            idx += 1
        sep_cnt -= 1
    else:
        origin[idx].append(address[i])
while len(origin[-1]) < 4:
    origin[-1].insert(0, '0') # 앞을 '0'으로 채워줌

[print(''.join(origin[i]), ':', sep='', end='') for i in range(7)]
print(''.join(origin[-1]))

