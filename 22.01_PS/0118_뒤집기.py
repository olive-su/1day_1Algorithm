from sys import stdin

S = stdin.readline().rstrip()
cnt = [0, 0] # 0과 1 덩어리를 세서 담아두는 임시 리스트
cnt[int(S[0])] += 1 # for 문에서 out of Index Error 방지를 위해 맨 앞 문자열 미리 처리

for i in range(1, len(S)):
    if S[i] != S[i-1]: # 앞 숫자랑 다른 숫자면 새로운 덩어리 시작임
        cnt[int(S[i])] += 1

print(min(cnt)) # 0과 1 덩어리 중 더 적은 덩어리 개수 출력
