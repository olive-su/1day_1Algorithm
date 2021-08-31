n = int(input())
rst = [n // 5, n // 5]
rst[1] += n % 5 // 3
if n % 5 % 3: # 나머지 존재
  # 기존 5의 몫에서 1씩 줄이면서 3으로 나눠지는 수가 있는 지 검사
    for i in range(1, rst[0] + 1):
        m = (n % 5) + (5 * i)
        rst[1] = (n // 5 - i) + (m // 3)
        if m % 3 == 0:
            exit(print(rst[1]))
    print(-1)
else: print(rst[1])
