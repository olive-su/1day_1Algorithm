from sys import stdin
N = int(stdin.readline())
ropes = []
cnt, rst = 0, 0
for _ in range(N):
    ropes.append(int(stdin.readline()))
ropes.sort(reverse=True)
for rope in ropes:
    cnt += 1
    weight = rope * cnt
    if max(weight, rst) == weight:
        rst = weight
print(rst)
