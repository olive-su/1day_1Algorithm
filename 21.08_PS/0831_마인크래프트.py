from sys import stdin
N, M, B = map(int, stdin.readline().split())
land = []
total = 0

for _ in range(N):
    arr = list(map(int, stdin.readline().split()))
    for a in arr:
        land.append(a) # 1차원으로 flatten
height = min(land)
sec_list = []
max_land = max(land)

def minecraft(land, block, height):
    sec = 0
    for i in range(N * M):
        # 블록을 제거하는 경우
        if land[i] > height:
            sec += 2 * (land[i] - height)
            block += land[i] - height
        # 블록을 추가하는 경우
        else:
            sec += 1 * (height - land[i])
            block += land[i] - height
    if block < 0:
        return -1
    return sec

# 가지고 있는 블록으로 놓을 수 있는 지 판단
while height <= max_land:
    block = B
    sec = minecraft(land, block, height)
    if sec == -1:
        break
    sec_list.append((sec, height))
    height += 1

# 땅 높이를 기준으로 정렬한 뒤 가장 최소 시간이 소요되는 작업 출력
sec_list.sort(reverse=True, key=lambda x : x[1])
sec_list.sort(key=lambda x : x[0])
print(sec_list[0][0], sec_list[0][1])
