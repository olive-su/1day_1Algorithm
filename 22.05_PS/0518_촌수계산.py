'''
dfs
부모노드 - 자식노드 상관없이 모두 relation 리스트에 연결 상태 저장
'''

import sys

input = sys.stdin.readline
n = int(input())
x, y = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

def dfs(cnt, start):
    visited[start] = True
    for i in relation[start]:
        if i == y: # 타깃 노드 발견시 프로그램 종료 -> cnt 값이 가장 최솟값일 경우
            sys.exit(print(cnt))
        if not visited[i]: 
            dfs(cnt + 1, i)

dfs(1, x)

print(-1)
