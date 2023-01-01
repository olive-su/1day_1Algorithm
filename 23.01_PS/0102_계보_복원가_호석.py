#boj. 21276
#time: 27'

import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n = int(input())
person = sorted(input().split())
root = []
indegree = defaultdict(int)
graph = defaultdict(list)
answer = defaultdict(list)
m = int(input())

for _ in range(m):
    x, y = input().split()
    indegree[x] += 1
    graph[y].append(x)

queue = deque([])
for p in person:
    if indegree[p] == 0: # 시조 이름 저장
        queue.append(p)
        root.append(p)

while queue:
    parent = queue.popleft()
    for child in graph[parent]:
        indegree[child] -= 1
        if indegree[child] == 0:
            answer[parent].append(child)
            queue.append(child)

print(len(root))
[print(r, end=' ') for r in sorted(root)]
print()

for p in person:
    children = sorted(answer[p])
    print(p, end=' ')
    print(len(children), end=' ')
    if len(children) > 0: [print(c, end=' ') for c in children]
    print()

