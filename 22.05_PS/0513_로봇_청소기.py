import sys

input = sys.stdin.readline

# 북, 동, 남, 서 : 0, 1, 2, 3
rv = [-1, 0, 1, 0]
cv = [0, 1, 0, -1]

graph, rst = [], 1
n, m = map(int, input().split())
r, c, d = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))
graph[r][c] = 2 # 시작 위치 청소
'''
0: 청소 x
1: 벽
2: 청소 o
'''
while True:
    flag = 1
    for i in range(4):
        d = (d + 3) % 4
        nr, nc = r + rv[d], c + cv[d]
        if 0 <= nr < n and 0 <= nc < m: # 범위 벗어나는지 체크
            if graph[nr][nc] == 0: 
                r, c = nr, nc # 이동
                graph[nr][nc] = 2 # 청소
                rst += 1
                flag = 0
                break
    if flag: # 연속 네 번 실행
        nr, nc = r + rv[(d + 2) % 4], c + cv[(d + 2) % 4]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != 1:
            r, c = nr, nc
            if graph[nr][nc] == 0:
                rst += 1
                graph[nr][nc] = 2
        else:
            break
print(rst)
