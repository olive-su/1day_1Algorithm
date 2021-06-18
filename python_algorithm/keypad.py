def distance(left_now, center_now, right_now, hand):
    left_distance = abs(center_now[0] - left_now[0]) + abs(center_now[1] - left_now[1])
    right_distance = abs(center_now[0] - right_now[0]) + abs(center_now[1] - right_now[1])
    if left_distance < right_distance:
        return 'L' # 왼쪽 손 이동
    elif left_distance > right_distance:
        return 'R' # 오른쪽 손 이동
    else:
        if hand == "left" : return 'L'
        else : return 'R'# 왼쪽 손잡이 or 오른쪽 손잡이

def solution(numbers, hand):
    answer = ''
    # position = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    left_now = (0, 3)
    right_now = (2, 3)
    for i in range(len(numbers)):
        if numbers[i] == 0: # 0은 나눌 수 없으므로 따로 조건식을 만듦
            center_now = (1, 3)
            move = distance(left_now, center_now, right_now, hand)
            answer += move
            if move == 'L' : left_now = center_now
            else : right_now = center_now
                
        elif numbers[i] % 3 == 1: # 왼쪽 라인
            left_now = (0, (numbers[i] // 3))
            answer += 'L'
            
        elif numbers[i] % 3 == 0: # 오른쪽 라인
            right_now = (2, (numbers[i] // 4))
            answer += 'R'
            
        else:
            center_now = (1, (numbers[i] // 3))
            move = distance(left_now, center_now, right_now, hand)
            answer += move
            if move == 'L' : left_now = center_now
            else : right_now = center_now
    
    return answer
