def solution(weights, head2head):
    rank = []
    # rank = [번호, 몸무게, 횟수, 승률] 저장
    for idx, w in enumerate(weights):
        rank.append([idx + 1, w, 0, 0]) # 처음엔 횟수, 승률 0으로 초기화
    for w in range(len(weights)):
        total_game, win_game = 0, 0
        for h in range(len(head2head)):
            if head2head[w][h] == 'L' or head2head[w][h] == 'W':
                total_game += 1
                if head2head[w][h] == 'W':
                    win_game += 1
                    if weights[w] < weights[h]:
                        rank[w][2] += 1 # 횟수 +1
        if total_game:
            rank[w][3] = (win_game/total_game) * 100 # 승률
    rank.sort(reverse=True, key=lambda x : x[1]) # 몸무게 순 정렬
    rank.sort(reverse=True, key=lambda x : x[2]) # 횟수 순 정렬
    rank.sort(reverse=True, key=lambda x : x[3]) # 승률 순 정렬
    answer = []
    for r in rank:
        answer.append(r[0])
    return answer
