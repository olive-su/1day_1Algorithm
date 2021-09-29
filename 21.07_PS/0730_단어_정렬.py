import sys
n = int(sys.stdin.readline())
word = []
for _ in range(n):
   m = sys.stdin.readline().rstrip()
   if m not in word: # 중복 필터링
       word.append(m)
word.sort() # 사전 순 정렬
word.sort(key=lambda x : len(x)) # 길이 순 정렬
for i in word:print(i)
