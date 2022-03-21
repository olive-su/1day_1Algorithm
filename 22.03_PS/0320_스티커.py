from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    sticker = []
    sticker.append(list(map(int, stdin.readline().split())))
    sticker.append(list(map(int, stdin.readline().split())))
    d = [[sticker[0][0]], [sticker[1][0]]]
    d[0] += [0] * (n-1)
    d[1] += [0] * (n-1)
    before = max(d[0][0], d[1][0])
    for i in range(1, n):
        if i % 2:  # 홀수
            d[0][i] = max(before, d[1][i-1] + sticker[0][i])
            d[1][i] = max(before, d[0][i-1] + sticker[1][i])
        else: # 짝수
            d[1][i] = max(before, d[0][i-1] + sticker[1][i])
            d[0][i] = max(before, d[1][i-1] + sticker[0][i])
        before = max(d[0][i], d[1][i])
    print(before)
