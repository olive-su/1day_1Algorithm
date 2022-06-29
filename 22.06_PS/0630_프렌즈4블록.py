# programmers
# time : 53'

dx = [1, 0, 1]
dy = [0, 1, 1]

cnt = 0

def eraser(x, y, board, n, m):
    origin = board[y][x]
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[ny][nx] != origin:
                return False
        else:
            return False
    return True

def fill(x, y, erase, board):
    global cnt
    
    origin = board[y][x]
    if erase[y][x]: 
        erase[y][x] = 0
        cnt += 1
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if erase[ny][nx]: 
            erase[ny][nx] = 0
            cnt += 1
    return erase

def solution(m, n, board):
    answer = 0

    for b in range(len(board)):
        board[b] = list(board[b])
        
    
    flag = 1
    while flag:
        flag = 0
        erase = [board[i][:] for i in range(len(board))]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j]:
                    if eraser(j, i, board, n, m): # 지울 수 있는 영역
                        erase = fill(j, i, erase, board)
                        flag = 1
        board = erase
        # 180도 회전
        new = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[m-1-j][i] != 0:
                    new[i].append(board[m-1-j][i])
            if len(new[i]) < m:
                new[i] += [0] * (m - len(new[i]))
        
        for i in range(m):
            for j in range(n):
                board[i][j] = new[j][m - 1 - i]
    
    return cnt