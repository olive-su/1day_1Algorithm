# boj.1967
# time: 

import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
a, answer = 0, 0
n = int(input())
parent = [0 for _ in range(n + 1)] # arr[자식] = 부모
child = [[] for _ in range(n + 1)] # arr[부모] = [자식1, 자식2]
leaf = []

if n == 1: exit(print(0))

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    parent[c] = (p, w)
    child[p].append((c, w))

for i in range(1, n + 1):
    if i == 1 and len(child[1]) == 1: leaf.append(1)
    if len(child[i]) == 0: leaf.append(i) # 단말노드

def dfs(num, visited):
    global answer, a

    # 루트 노드 x & 부모 노드 미방문
    if num != 1:
        p, w = parent[num] # 부모, 부모까지의 가중치
        if visited[p] == -1:
            visited[p] = visited[num] + w # 현재 위치까지의 값 + 가중치
            dfs(p, visited) # 부모 방문

    # 쟈식 노드 방문
    for c, w in child[num]:
        if visited[c] == -1:
            visited[c] = visited[num] + w
            dfs(c, visited)
        
    if num in leaf:
        if answer < visited[num]:
            answer = visited[num]
            a = num
        return

visited = [-1 for _ in range(n + 1)]
visited[leaf[0]] = 0
dfs(leaf[0], visited)
answer = 0
visited = [-1 for _ in range(n + 1)]
visited[a] = 0
dfs(a, visited)

print(answer)
