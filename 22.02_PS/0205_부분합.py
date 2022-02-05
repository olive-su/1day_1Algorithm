from sys import stdin
n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
rst = 0  # 최소 길이의 값
now = 0  # 부분합 최대 값
end = -1

for i in range(n):
    now += arr[i]
    rst += 1
    if now >= s:
        end = i
        break

if end == -1:  # 부분합 s 존재 x
    rst = 0

for i in range(1, n):
    now -= arr[i - 1]  # 이전 인덱스 값 뺌
    if end + 1 < n:
        end += 1
        now += arr[end]  # 이후 인덱스 값 더함 (인덱스 범위 고려)
    elif now < s:
        break
    else:
        end = n - 1
        rst -= 1
    while now >= s:
        now -= arr[end]
        if now < s:  # 합이 s가 안되면 탐색 종료(rst 그대로)
            now += arr[end]
            break
        if end > 1:
            end -= 1
        if rst > 1:
            rst -= 1

print(rst)
