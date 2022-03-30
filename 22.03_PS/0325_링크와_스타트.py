import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
player, com = [], []
rst = 1e9
for _ in range(n):
    player.append(list(map(int, input().split())))
for i in range(1, n):
    [com.append(j) for j in combinations(range(0, n), i)]

# n + 1번 수행
for i in range(len(com) // 2):
    start = 0
    # start 팀
    for j in range(len(com[i]) - 1):
        for k in range(j + 1, len(com[i])):
            start += player[com[i][j]][com[i][k]]
            start += player[com[i][k]][com[i][j]]
    # link 팀
    l = len(com) - i - 1
    link = 0
    for j in range(len(com[l]) - 1):
        for k in range(j + 1, len(com[l])):
            link += player[com[l][j]][com[l][k]]
            link += player[com[l][k]][com[l][j]]
    rst = min(rst, abs(start-link))
print(rst)

