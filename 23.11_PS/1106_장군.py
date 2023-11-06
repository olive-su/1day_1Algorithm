from collections import deque

dx = [-2, 2, 3, 3, 2, -2, -3, -3]
dy = [-3, -3, -2, 2, 3, 3, 2, -2]
blocked_x = [[-1, 0], [1, 0], [2, 1], [2, 1],
             [1, 0], [-1, 0], [-2, -1], [-2, -1]]
blocked_y = [[-2, -1], [-2, -1], [-1, 0],
             [1, 0], [2, 1], [2, 1], [1, 0], [-1, 0]]
r1, c1 = map(int, input().split())  # 상 위치
r2, c2 = map(int, input().split())  # 왕 위치
visited = [[False] * 9 for _ in range(10)]
flag = False

queue = deque([(r1, c1, 0)])
while queue:
    y, x, w = queue.popleft()
    visited[y][x] = True
    if x == c2 and y == r2:
        print(w)
        flag = True
        break

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        blocked_nx1 = x + blocked_x[i][0]
        blocked_ny1 = y + blocked_y[i][0]
        blocked_nx2 = x + blocked_x[i][1]
        blocked_ny2 = y + blocked_y[i][1]

        if 0 <= nx < 9 and 0 <= ny < 10 and not visited[ny][nx]:
            if (blocked_nx1 != c2 or blocked_ny1 != r2) and (blocked_nx2 != c2 or blocked_ny2 != r2):
                queue.append((ny, nx, w + 1))

if not flag:
    print(-1)
