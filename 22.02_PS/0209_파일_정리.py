from sys import stdin
n = int(stdin.readline())
file, cnt = [], {}
for _ in range(n):
    file.append(stdin.readline().rstrip().split('.')[1])
for i in file:
    if cnt.get(i):
        cnt[i] += 1
    else:
        cnt[i] = 1
cnt = list(cnt.items())
cnt.sort()
[print(cnt[i][0], cnt[i][1], sep=' ') for i in range(len(cnt))]
