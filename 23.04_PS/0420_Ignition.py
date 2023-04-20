# boj. 13141
# time: 30'

# 각 노드까지 가는 거리가 가장 짧을 때

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
distance = [ [INF for _ in range(n + 1)] for _ in range(n + 1)] 
line = [] # 남은 줄 길이, start_node, end_node
node = [[] for _ in range(n + 1)] 
burn = set()
time = 0

for _ in range(m):
    s, e, l = map(int, input().split())
    distance[s][e] = min(distance[s][e], l)
    distance[e][s] = min(distance[e][s], l)
    node[s].append(len(line)) # 줄 번호
    node[e].append(len(line))
    line.append([l, s, e])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: distance[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost = distance[i][k] + distance[k][j]
            if cost < distance[i][j]: distance[i][j] = cost

fast_load = (INF, 0)
for i in range(1, n + 1):
    total_cost = sum(distance[i]) - INF 
    if total_cost < fast_load[0]:
        fast_load = (total_cost, i)

burn.add(fast_load[1])

# 양쪽에서 타들어가는 경우 : (- 0.5)

def sum_line():
    rst = 0
    for l in line:
        rst += l[0]
    return rst

while sum_line():
    time += 1
    burned = []
    flag = False
    new_burn = []
    for b in burn:
        for i in node[b]:
            if not line[i][0]: # 이미 다 타버린 상태(또 태우려험)
                if i in burned: flag = True
            else:
                line[i][0] -= 1 # 길이 -1
                burned.append(i)
                if not line[i][0]:
                    new_burn.append(line[i][1])
                    new_burn.append(line[i][2])
    for i in new_burn:
        burn.add(i)

if flag: 
    print(time - 0.5)
else:
    print(float(time))