num = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
call = 0
string = list(input())
for i in string:
    for j in range(len(num)):
        if i in num[j]:
            call += j
            break
print(call)
