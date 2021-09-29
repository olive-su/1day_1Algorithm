n = int(input())
score = list(map(int, list(input().split())))
score = list(map(lambda x : x/max(score)*100, score))
print(sum(score) / n)
