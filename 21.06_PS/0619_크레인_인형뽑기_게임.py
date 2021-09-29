def pop_stack(stack): # 스택에 쌓인 요소 제거하는 함수
    if (len(stack) >= 2 ): # IndexError 방지 위함
        if stack[len(stack) - 1] == stack[len(stack) - 2]:
            del stack[-2:] # 맨 끝 요소 2개 제거
            return 2
    return 0

def solution(board, moves):
    answer = 0
    stack = []
    for move in range(len(moves)): # i : 높이, moves[move] : 라인 번호
        i = 0
        while (i < len(board) and board[i][moves[move] - 1] == 0): # 인덱스 값들로 계산해야하므로 -1을 해줌
            i += 1
        if i == len(board): # 모든 칸이 0으로 차있으면 아무일도 발생하지 않음
            continue
        stack.append(board[i][moves[move] - 1]) # 뽑은 인형의 번호 스택에 추가
        board[i][moves[move] - 1] = 0 # 인형이 뽑힌 칸에 0 저장
        answer += pop_stack(stack)
        
    return answer
