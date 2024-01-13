from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 모서리 방문 처리를 위해 기존 맵의 2배 길이로 입력을 받음
    graph = [[-1 for _ in range(102)] for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if y1 < y < y2 and x1 < x < x2:
                    graph[y][x] = 0
                elif graph[y][x] != 0:
                    graph[y][x] = 1  # 테두리 부분만 표시

    visited = [[-1 for _ in range(102)] for _ in range(102)]

    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2

    queue = deque()
    queue.append((cy, cx))
    visited[cy][cx] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 102 and 0 <= nx < 102 and graph[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

    return visited[iy][ix] // 2
