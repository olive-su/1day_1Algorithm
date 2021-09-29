x = int(input())
for _ in range(x):
    y = list(input())
    valid = 0
    for i in y:
        if i == '(': valid += 1
        elif i == ')': valid -= 1
        if valid < 0:
            break
    if valid == 0 : print("YES")
    else: print("NO")
