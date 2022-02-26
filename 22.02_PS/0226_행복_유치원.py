from sys import stdin

n, k = map(int, stdin.readline().split())
kids = list(map(int, stdin.readline().split()))
com = []
for i in range(1, n):
    com.append(kids[i] - kids[i - 1])
com.sort()
print(sum(com[:n-k]))
