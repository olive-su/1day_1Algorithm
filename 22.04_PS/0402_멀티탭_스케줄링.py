import sys

input = sys.stdin.readline
n, k = map(int, input().split())
products = list(map(int, input().split()))
cnt = 0
plug = [[] for _ in range(n)]
idx = 0
for i in range(k):
    waiting = 0
    if products[i] in plug:
        continue
    else:
        if plug[-1]: # 더 이상 플러그 꽂을 공간이 없을 때
            rst = 0
            for j in range(n):
                cnt_value = products[i+1:].count(plug[j])
                if cnt_value == 0: # 한번도 등장하지 않는 경우 
                    rst = j
                    break
                else:
                    for l in range(i+1, k):
                        if plug[j] == products[l]:
                            appear = l # 처음 등장하는 인덱스
                            break
                    if appear > waiting:
                        waiting = appear
                        rst = j
            plug[rst] = products[i]
            cnt += 1
        else:
            plug[idx] = products[i]
            idx += 1
print(cnt)
            