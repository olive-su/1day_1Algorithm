from sys import stdin
N, C = map(int, stdin.readline().split())
router = []
for _ in range(N):
    router.append(int(stdin.readline()))
router.sort()
start = 1
end = router[-1] - router[0]
rst = 0
while( start <= end ):
    mid = ( start + end ) // 2
    before = router[0]
    cnt = 1
    for i in range(1, N):
        if router[i] >= before + mid:
            before = router[i] # 이전 공유기 위치 갱신
            cnt += 1 # 공유기 설치
        if cnt >= C:
            rst = mid
            start = mid + 1
            break
    if cnt < C:
        end = mid - 1
print(rst)
