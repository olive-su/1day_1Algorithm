# programmers

'''
대소문자 구분 x
같으면 number
'''
def head(file):
    rst = ''
    for i in file:
        if i.isdigit():
            break
        rst += i.upper()
    return rst

def number(file):
    rst = 0
    flag = 0
    for i in file:
        if flag and i.isalpha(): # tail 나오는 부분
            break
        if i.isdigit():
            flag = 1
            rst = rst * 10 + int(i)
    return rst


def solution(files):
    files.sort(key = number)
    files.sort(key = head)
    
    return files
