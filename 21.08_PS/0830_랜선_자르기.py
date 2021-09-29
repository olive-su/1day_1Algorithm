from sys import stdin
K, N = map(int, stdin.readline().split())
line = []
rst = []
for _ in range(K):
    line.append(int(stdin.readline()))

start = 1
end = sum(line) // N
while start<=end:
    middle = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += line[i] // middle
    if cnt < N:
        end = middle-1
    else:
        start = middle+1
print(end)
