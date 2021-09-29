from sys import stdin
n = stdin.readline()
N = list(map(int, stdin.readline().split()))
m = stdin.readline()
M = list(map(int, stdin.readline().split()))

set_M = set(M)
dic_M = {}
for i in set_M:
    dic_M[i] = 0
for j in N:
    if dic_M.get(j) != None:
        dic_M[j] += 1
answer = []
for i in M:
    if dic_M.get(i) != None:
        answer.append(dic_M[i])
    else:
        answer.append(0)
answer = list(map(str, answer))
print(' '.join(answer))
