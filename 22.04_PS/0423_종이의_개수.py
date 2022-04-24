import sys

input = sys.stdin.readline
n = int(input())
graph = []
cnt = {'-1':0, '0':0, '1':0}
for _ in range(n):
    graph.append(input().split())

def check(x, y, s, t):
    for i in range(y, y + s):
        for j in range(x, x + s):
            if graph[i][j] != t:
                return False
    return True
size = n // 3
x, y = 0, 0
def paper(x, y, size):
    for i in range(y, y + size + size + 1, size):
        for j in range(x, x + size + size + 1, size):
            target = graph[i][j]
            if check(j, i, size, target): # 한 칸이 모두 같은 모양일 때
                cnt[target] += 1
            else:
                paper(j, i, size//3) # 다른 모양이 섞여있을 경우, 다시 재귀

target = graph[0][0]
if check(0, 0, n, target):
    cnt[target] = 1
else: paper(0, 0, size)
[print(i) for i in list(cnt.values())]