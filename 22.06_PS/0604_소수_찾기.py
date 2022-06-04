# 프로그래머스 완전탐색

import math
import copy

def prime(num):
    s = set()
    str_num = list(str(num))
    
		# 에라토스테네스의 체
    array = [True] * (num + 1)
    for i in range(2, int(math.sqrt(num)) + 1):
        if array[i] == True: # 소수일 경우
            j = 2
            while i * j <= num:
                array[i * j] = False
                j += 1

    for i in range(2, num + 1):
        if array[i]: # 소수인 경우만 탐색 시작
            flag = 0
            v = copy.deepcopy(str_num) # 리스트라서 deepcopy로 리스트 자체를 복사
            for j in list(str(i)):
                if j not in v: # numbers의 수들로 만들 수 없는 경우 break
                    flag = 1
                    break
                else: v.remove(j) # 이미 체크한 숫자 삭제
            if flag: continue
            else:
                s.add(i)
    return len(s)
    

def solution(numbers):
    s_numbers = sorted(list(numbers), reverse=True) 
		# 정렬 -> 가장 큰 수까지 에라토스테네스의 체 적용하기 위함
    answer = prime(int(''.join(s_numbers)))
    return answer