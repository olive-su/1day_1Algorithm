import sys

cnt = 0
x = list(sys.stdin.readline().split())
num, goal = int(x[0]), int(x[1])
coin = []
for _ in range(num):
    input = int(sys.stdin.readline())
    if input <= goal:
        coin.append(input)
while goal:
    cnt += goal // coin[-1]
    goal -= coin[-1] * (goal // coin.pop())
print(cnt)
