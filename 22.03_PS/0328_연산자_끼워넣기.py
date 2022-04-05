import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_v, min_v = -1e9, 1e9


def dfs(cnt, rst, add, sub, mul, div):
    global max_v, min_v
    if cnt == n:
        max_v = max(max_v, rst)
        min_v = min(min_v, rst)
        return
    if add:
        dfs(cnt + 1, rst + arr[cnt], add - 1, sub, mul, div)
    if sub:
        dfs(cnt + 1, rst - arr[cnt], add, sub - 1, mul, div)
    if mul:
        dfs(cnt + 1, rst * arr[cnt], add, sub, mul - 1, div)
    if div:
        if rst < 0 and arr[cnt]: # 음수를 양수로 나눌 경우
            dfs(cnt + 1, -(abs(rst) // arr[cnt]), add, sub, mul, div - 1)
        else:
            dfs(cnt + 1, rst // arr[cnt], add, sub, mul, div - 1)

dfs(1, arr[0], add, sub, mul, div)
print(max_v)
print(min_v)
