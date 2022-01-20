S = input()
total = 0
alpha = []
for i in S:
    if i.isdigit():
        total += int(i)
    else:
        alpha += i
alpha.sort()
print(''.join(alpha)+str(total))
