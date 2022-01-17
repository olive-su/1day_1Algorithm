from sys import stdin

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))
group = [0 for i in range(N)] # 모험가의 수를 담아두는 임시 리스트

P.sort(reverse=True)

for i in range(N):
    g = i
    while g < N:
        if P[g] <= (N - g): # 남은 모험가의 수
            g += P[g]
            group[i] += 1
        else:
            break        

print(max(group)) # 나온 모험가 구성원의 수 중 가장 높은 수 출력
