from sys import stdin

n = list(stdin.readline().rstrip())
n.sort()
set_n = set(n)
set_n = list(set_n)
rst_f, rst_e = '', ''
center = ''


if len(n) % 2 == 0:
    flag = 1
else:
    flag = 0

for i in range(len(set_n)):  # 팰린드롬 문자가 가능한 지 검사
    if n.count(set_n[i]) % 2 == 0:
        continue
    else:
        if flag:
            print("I'm Sorry Hansoo")
            exit()
        else:  # 글자수 홀수 & 개수 홀수인 경우 한번까지는 가능
            flag = 1
            center = set_n[i]
if center:
    n.remove(center)
for i in range(0, len(n), 2):
    rst_f += n[i]
    rst_e += n[i + 1]
rst_e = list(rst_e)
rst_e.reverse()
if center:
    print(rst_f + center + ''.join(rst_e))
else:
    print(rst_f + ''.join(rst_e))

