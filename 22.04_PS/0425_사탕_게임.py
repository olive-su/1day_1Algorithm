import sys

input = sys.stdin.readline
n = int(input())
# 방향 벡터 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
ans = 0

# 최대 길이를 구하는 함수
def max_length():
    global ans
    for i in range(n):
        cnt_col, cnt_row = 1, 1
        target_col = graph[i][0] # 한 행의 맨 첫 번째 원소 값
        target_row = graph[0][i] # 한 열의 맨 첫 번째 원소 값
        for j in range(1, n):
            if target_col == graph[i][j]:
                cnt_col += 1
            else:
                target_col = graph[i][j]
                cnt_col = 1
            if target_row == graph[j][i]:
                cnt_row += 1
            else:
                target_row = graph[j][i]
                cnt_row = 1
            ans = max(cnt_col, ans)
            ans = max(cnt_row, ans)

for i in range(n):
    for j in range(1, n):
        if graph[i][j] != graph[i][j - 1]: # 같은 열 내에 인접한 칸에 들어있는 문자열이 다를 경우
            tmp = graph[i][j] 
            graph[i][j] = graph[i][j - 1]
            graph[i][j - 1] = tmp
            max_length()
            graph[i][j - 1] = graph[i][j]
            graph[i][j] = tmp

for i in range(n):
    for j in range(1, n):
        if graph[j][i] != graph[j - 1][i]: # 같은 행 내에 인접한 칸에 들어있는 문자열이 다를 경우
            tmp = graph[j][i] 
            graph[j][i] = graph[j - 1][i]
            graph[j - 1][i] = tmp
            max_length()
            graph[j - 1][i] = graph[j][i]
            graph[j][i] = tmp

print(ans)