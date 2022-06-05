# time : 9'
from collections import deque

# 프로그래머스 dfs/bfs

'''
graph: 그래프 연결상태
start: 시작노드
visited: 방문여부
'''

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        s = q.popleft()
        for i in range(len(visited)):
						# s <-> i 연결된 상태이며 아직 i 노드를 방문하지 않은 경우
            if graph[s][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return visited
        

def solution(n, computers):
    visited = [0] * (n)
    rst = 0
    for i in range(n):
        if not visited[i]: # 아직 방문하지 않은 노드가 있을 경우
            visited = bfs(computers, i, visited)
            rst += 1
    
    return rst