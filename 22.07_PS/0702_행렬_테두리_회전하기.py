# programmers
# time : 25'

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotation(sx, sy, ex, ey, arr):
    dv = 0
    tmp = arr[sx][sy]
    rst = tmp
    x, y = sx, sy
    
    while True:
        nx, ny = x + dx[dv], y + dy[dv]
        if sx <= nx <= ex and sy <= ny <= ey:
            a = arr[nx][ny]
            arr[nx][ny] = tmp
            tmp = a
            rst = min(rst, tmp)
            x, y = nx, ny
        else:
            dv += 1
        if x == sx and y == sy:
            break
    return arr, rst


def solution(rows, columns, queries):
    answer = []
    maps = []
    n = 1
    for _ in range(rows):
        maps.append([])
        for _ in range(columns):
            maps[-1].append(n)
            n += 1
    
    for q in queries:
        x1, y1, x2, y2 = q
        maps, rst = rotation(x1 - 1, y1 - 1, x2 - 1, y2 - 1, maps)
        answer.append(rst)
    
    return answer