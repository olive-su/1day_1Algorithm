"""
Greedy Algorithm
최적 부분 구조
: '+'연산을 먼저 수행하고 '-'연산을 수행하는게 가장 최적의 값을 도출할 수 있음
"""
import sys

num, m = '', []
n = list(sys.stdin.readline().rstrip())
for i in range(len(n)): # 피연산자와 연산자로 나눠서 리스트에 담음
    if n[i] == '+' or n[i] == '-':
        m.append(int(num)) # 연산자를 만나기 이전 문자들은 모두 숫자이므로 num을 리스트에 추가
        num = '' # 숫자를 담는 변수 초기화
        m.append(n[i])
    else:
        num += n[i]
m.append(int(num)) # 맨 마지막 숫자 처리
while '+' in m:
'''
Ex. list = [55, '-', 50, '+', 40]
m[2](현재 값 50)에 두 숫자의 합을 저장하고 ['+', 40]은 제거 
'''
    j=m.index('+')
    m[j-1] = m[j-1] + m[j+1] 
    m.pop(j)
    m.pop(j)
while len(m) > 1:
'''
이제 남은 연산자가 '-'뿐이므로 남은 연산들 모두 수행
'''
    m[0] = m[0] - m[2]
    m.pop(1)
    m.pop(1)
print(m[0])
