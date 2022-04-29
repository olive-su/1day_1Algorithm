import sys

input = sys.stdin.readline
n = int(input())
# 'A' : ['부모 노드', '왼쪽 자식 노드', '오른쪽 자식 노드']
graph = {'A':['.', ],} # 루트 노드는 부모 노드가 없음
visited = [0] * n
for _ in range(n):
    root, ln, rn = input().split()
    graph[root].append(ln)
    graph[root].append(rn)
    if ln != '.' : graph[ln] = [root]
    if rn != '.' : graph[rn] = [root]

opt = 'A'
while True: # 맨 왼쪽 노드
    if graph[opt][1] == '.':
        break
    opt = graph[opt][1]

cnt = 0

def preorder(cnt, now):
    if graph[now] == 

