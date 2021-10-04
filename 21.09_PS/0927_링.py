n = int(input())
ring = list(map(int, input().split()))
for i in range(1, n):
    first = ring[0]
    second = ring[i]
    for j in range(ring[i], 1, -1):
        if first % j == 0 and second % j == 0:
            first //= j
            second //= j
        if second == 1:
            break
    print(first, '/', second, sep='')

