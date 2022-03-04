from sys import stdin

input = stdin.readline
n = int(input())
d = []
for _ in range(n + 1):
    d.append([1] * 10)

# n = 0일때는 이미 이전에 1로 다 초기화를 해줬기 때문에 반복문 돌필요 없음
for i in range(1, n+1):
    for j in range(10):
        d[i][j] = sum(d[i - 1][:j + 1]) % 10007
print(d[-1][-1])

