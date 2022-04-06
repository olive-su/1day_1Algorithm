import sys

input = sys.stdin.readline
n, k = map(int ,input().split())
rst = 0
repeat = 0
word = []
dict = {'a':1, 'n':1, 't':1, 'i':1, 'c':1} # 이미 배운 글자 목록

for _ in range(n):
    inputs = input().rstrip()[4:-4]
    word.append(inputs)
    for i in inputs:
        if i not in dict:
            repeat += 1
            dict[i] = 0

dict_keys = list(dict.keys())

if repeat and k < 6: # 단어를 배울 수 없는 경우
    sys.exit(print(0))

repeat = min(repeat, k - 5)
if repeat < 0: repeat = 0

def dfs(repeat, idx):
    global rst
    cnt = 0
    if repeat == 0:
        for i in word: # 읽을 수 있는 단어 셈
            flag = 1
            for j in i:
                if not dict[j]: # 아직 배우지 않은 글자
                    flag = 0
                    break
            cnt += flag
        rst = max(rst, cnt)
        return
        
    for i in range(idx, len(dict)):
        if dict[dict_keys[i]] == 0:
            dict[dict_keys[i]] = 1
            dfs(repeat-1, i)
            dict[dict_keys[i]] = 0

dfs(repeat, 5)
print(rst)