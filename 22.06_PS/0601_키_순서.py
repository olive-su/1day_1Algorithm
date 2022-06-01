'''
row 한줄이 모두 True인 경우 -> 각 학생별로 키 순서 비교가능
'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = [[False] * (n + 1) for _ in range(n + 1)]
rst = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            height[i][j] = True

for _ in range(m):
    a, b = map(int, input().split())
    height[a][b] = True

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if height[i][k] == True and height[k][j] == True:
                height[i][j] = True

for i in range(1, n + 1):
    flag = 0
    for j in range(1, n + 1):
        if height[i][j] or height[j][i]:
            flag += 1
    if flag == n:
        rst += 1

print(rst)


