num = 1
while num <= 10000:
    flag = 1
    digit_num = len(str(num)) * 9
    for i in range(digit_num, 0, -1):
        if num - i > 0:
            if sum(list(map(int, str(num - i)))) == i:
                flag = 0
                break
    if flag: print(num)
    num += 1
