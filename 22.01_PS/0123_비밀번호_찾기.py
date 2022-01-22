from sys import stdin
N, M = map(int, stdin.readline().split())
pw_dic = {}
search = []
for i in range(N):
    key, value = stdin.readline().split()
    pw_dic[key] = value
for j in range(M):
    search.append(stdin.readline().rstrip())
for l in range(M):
    s = search[l]
    print(pw_dic.get(s))
