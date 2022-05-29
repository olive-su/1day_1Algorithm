import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
words, weight, dicts = [], defaultdict(int), {}
rst = 0

for _ in range(n):
    w = list(input().rstrip())
    words.append(w)
    # 자릿수에 따른 가중치 값을 weight에 저장
    for i in range(len(w) - 1, -1, -1):
        weight[w[i]] += 10 ** (len(w) - i)

# 저장된 가중치 값에 따라 역순으로 정렬 수행
weights = sorted(weight.items(), key=lambda x : x[1], reverse=True)

# dicts에 알파벳 가중치에 따라 0~9까지 숫자 대입
rank = 9
for i, j in weights:
    dicts[i] = str(rank)
    rank -= 1

# 입력된 단어를 숫자로 바꿈
for word in words:
    num = ''
    for j in word:
        num += dicts[j]
    rst += int(num)

print(rst)