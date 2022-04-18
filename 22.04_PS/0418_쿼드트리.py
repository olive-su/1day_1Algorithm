import sys

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

def tree(y, x, size):
    if size == 1:
        return graph[y][x]
    rst = ''
    flag = 0
    init_color = graph[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != init_color:
                flag = 1
    if flag:
        for i in range(4):
            ny = y + dy[i] * (size // 2)
            nx = x + dx[i] * (size // 2)
            string = tree(ny, nx, size // 2)
            if len(string) == 1:
                rst += string
            else:
                rst += '('+string+')'
    else:
        return init_color
    return rst
ans = tree(0, 0, n)
if len(ans) == 1:
    print(ans)
else:
    print('('+ans+')')
