# boj. 3665
# time : 26'

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    answer = []
    n = int(input())
    t = list(map(int, input().split()))
    team = {}
    for i in range(n):
        team[t[i]] = [i + 1, i]# 등수, team의 indegree 개수
    rank_change = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if team[a][0] < team[b][0]:
            team[a][1] += 1
            team[b][1] -= 1
        else:
            team[b][1] += 1
            team[a][1] -= 1

    t = list(team.items())
    t.sort(key = lambda x : x[1][1])
    answer = [(t[0][0], t[0][1][1])]
    flag = 0
    for i in range(1, n):
        if answer[-1][1] == t[i][1][1]:
            flag = 1
            break
        else: answer.append((t[i][0], t[i][1][1]))
    if flag: print('IMPOSSIBLE')
    else: 
        [print(i[0], end= ' ') for i in answer]
        print("")


