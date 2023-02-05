# boj. 17299
# time : 22' 

import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr_cnt = []
stack = []
answer = []
arr_cnt = dict(Counter(arr))
for a in range(n - 1, -1, -1):
    flag = False
    while stack:
        num, cnt = stack[-1]
        if cnt <= arr_cnt[arr[a]]: stack.pop() # 개수가 더 적거나 같으면 pop
        else: 
            answer.append(num)
            stack.append((arr[a], arr_cnt[arr[a]]))
            flag = True
            break
    if flag: continue
    answer.append(-1)
    stack.append((arr[a], arr_cnt[arr[a]]))

[print(answer[i], end=' ') for i in range(n - 1, -1, -1)]


