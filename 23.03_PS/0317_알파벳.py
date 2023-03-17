# boj. 1987
# time : 43'

import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
graph, visited, rst = [], [], 0

r, c = map(int, input().split())
alph_dict = [False] * 26

for _ in range(r):
    graph.append(input().rstrip())
    visited.append([False] * c)

def dfs(y, x, cnt):
    global rst 

    rst = max(rst, cnt)
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
            ord_num = ord(graph[ny][nx]) - 65
            if not alph_dict[ord_num]:
                visited[ny][nx] = True
                alph_dict[ord_num] = True
                dfs(ny, nx, cnt + 1)
                alph_dict[ord_num] = False
                visited[ny][nx] = False

visited[0][0] = True
alph_dict[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)

print(rst)