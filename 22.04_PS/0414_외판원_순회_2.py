import sys

input = sys.stdin.readline
n = int(input())
city = []
visited = [0] * n
rst = 1e9
for _ in range(n):
    city.append(list(map(int, input().split())))

distance = 0

def backtracking(idx, cnt, total):
    global rst
    if cnt == n - 1:
        if city[idx][0]:
            rst = min(rst, total + city[idx][0])
            return
    for i in range(1, n):
        if not visited[i]:
            if city[idx][i]:
                visited[i] = 1
                backtracking(i, cnt + 1, total + city[idx][i])
                visited[i] = 0

backtracking(0, 0, 0)

print(rst)
