from sys import stdin
from collections import Counter
num1 = 0
num2 = 0
t = stdin.readline().rstrip()
cnt_t = Counter(t)
if '6' in t or '9' in t:
    cnt_629 = cnt_t['6'] + cnt_t['9']
    cnt_t['6'] = cnt_629 // 2
    cnt_t['9'] = cnt_629 // 2
    if cnt_629 % 2 != 0:
        cnt_t['6'] += 1
        cnt_t['9'] += 1
print(max(cnt_t.values()))
