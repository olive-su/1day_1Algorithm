from sys import stdin

n = int(stdin.readline())
a, b = [], []
for _ in range(n):
    a.append(tuple(map(int, stdin.readline().split())))
a.sort(reverse = True, key = lambda x : x[0]) 
# 회의가 시작하자 마자 끝나는 경우 고려하기 위해 우선 시작 시간이
# 빠른 회의가 먼저 선택되도록 시작시간 기준으로 정렬
a.sort(reverse = True, key = lambda x : x[1])
# pop()로 복잡도 줄이기 위해 reverse=True 진행
time = 0
while a:
    c = a.pop()
    if c[0] >= time:
        b.append(c)
        time = c[1]
print(len(b))
