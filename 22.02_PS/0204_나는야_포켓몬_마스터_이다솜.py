from sys import stdin
n, m = map(int, stdin.readline().split())
dic1, dic2 = {}, {}
for i in range(1, n + 1):
    input = stdin.readline().rstrip()
    dic1[i] = input  # key : 숫자, value : 문자
    dic2[input] = i  # key : 문자, value : 숫자
for _ in range(m):
    search = stdin.readline().rstrip()
    if search.isdigit():  # 숫자일 경우
        print(dic1[int(search)])
    else:  # 문자일 경우
        print(dic2[search])
