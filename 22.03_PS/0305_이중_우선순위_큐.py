from sys import stdin
from heapq import *

t = int(stdin.readline())
for _ in range(t):
    k = int(stdin.readline())
    p_queue = []
    pr_queue = []
    v = {}  # 삭제됐는지 확인하는 딕셔너리
    flag = 0
    for _ in range(k):
        c = stdin.readline().split()
        command = c[0]
        param = c[1]
        if command == "I":
            param = int(param)
            heappush(p_queue, param)
            heappush(pr_queue, (-param, param))
            if v.get(param):
                v[param] += 1  # 중복 값 처리
            else:
                v[param] = 1
        else:
            if param == '1':
                if pr_queue:
                    p = heappop(pr_queue)[1]
                    while pr_queue and not v.get(p):
                        p = heappop(pr_queue)[1]
                    if v.get(p):
                        v[p] -= 1

            else:
                if p_queue:
                    p = heappop(p_queue)
                    while p_queue and not v.get(p):
                        p = heappop(p_queue)
                    if v.get(p):
                        v[p] -= 1
    while pr_queue:
        rst = heappop(pr_queue)[1]
        if v[rst]:
            print(rst, end=' ')
            flag = 1
            break
    if not flag:
        print("EMPTY")
        continue
    while p_queue:
        rst = heappop(p_queue)
        if v[rst]:
            print(rst)
            break
