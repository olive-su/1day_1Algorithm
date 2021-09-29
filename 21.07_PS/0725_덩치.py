import sys

n = int(sys.stdin.readline().rstrip())
profile, answer = [], []
for i in range(n):
    person = sys.stdin.readline().rstrip().split()
    profile.append((int(person[0]), int(person[1])))

for j in range(n):
    rank = 1
    for k in range(n):
        if profile[k][0] > profile[j][0] and profile[k][1] > profile[j][1]:
            rank += 1
    answer.append(rank)

print(' '.join(list(map(str, answer))))
