from copy import deepcopy
import sys

input = sys.stdin.readline
n = int(input())
older_arr = []
[older_arr.append([i]) for i in range(10)]
ans = list(range(10))
newer_arr = [[] for _ in range(10)]
cnt = 10
while cnt <= n:
    if ans[-1] == 9876543210:
        sys.exit(print(-1))
        break
    newer_arr = [[] for _ in range(10)]
    for i in range(10):
        for j in range(i):
            if len(older_arr[j]) == 0: continue
            for k in older_arr[j]:
                t = int(str(i) + str(k))
                newer_arr[i].append(t)
                cnt += 1
                ans.append(t)
    older_arr = deepcopy(newer_arr)
print(ans[n])
