from sys import stdin
N, M = map(int, stdin.readline().split())
hear_list, see_list = {}, []
for _ in range(N):
    hear_list[stdin.readline().rstrip()] = 1
for _ in range(M):
    name = stdin.readline().rstrip()
    if hear_list.get(name):
        see_list.append(name)
see_list.sort()
print(len(see_list))
[print(i) for i in see_list]
