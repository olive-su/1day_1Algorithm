import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

visited = [0] * n

def backtracking(cnt, idx):
    if cnt == m:
        rst = []
        for i in range(n):
            if visited[i]:
                rst.append(arr[i])
        if rst not in ans:
            ans.append(rst)
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            backtracking(cnt + 1, i + 1)
            visited[i] = 0

backtracking(0, 0)
for i in ans:
    print(' '.join(map(lambda x : str(x), i)))