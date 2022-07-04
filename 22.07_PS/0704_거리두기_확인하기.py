
'''
5 * 5 * 5
|r1 - r2| + |c1 - c2| 
맨해튼 거리 2 이하 불가
아래 파티션 확인 - 두칸 아래 확인
우측 파티션 확인 - 두칸 오른쪽 확인
대각선 확인 - 파티션 개수 확인
'''

dx = [0, 1, 0, 2, 1, -1]
dy = [1, 0, 2, 0, 1, 1]


def check(y, x, graph):
    part = [0, 0]
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if i == 4: # 우측 아래 위치 처리
                if graph[ny][nx]  == 'P' and sum(part) < 2:
                    return 0
            elif i == 5: # 좌측 아래 위치 처리
                if graph[ny][nx] == 'P':
                    if graph[ny - 1][nx] == 'O' or graph[ny][nx + 1] == 'O':
                        return 0
            else:
                if i < 2: # 우측 + 1, 아래 + 1 확인
                    if graph[ny][nx] == 'P':
                        return 0
                    if graph[ny][nx] == 'X':
                        part[i] = 1
                else: # 우측 + 2, 아래 + 2 확인
                    if graph[ny][nx] == 'P' and part[i%2] == 0: # 0 P
                        return 0
                    
    return 1


# 옳은 지도 : 1, 옳지 않은 지도 0
def solution(places):
    answer = []
    for i in range(5):
        flag = 1
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P': # 사람이 앉아있는 칸만 검사 
                    flag = check(j, k, places[i])
                    if not flag: break
            if not flag: break
        answer.append(flag)

    return answer