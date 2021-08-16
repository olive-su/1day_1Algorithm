from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    h = list(map(int, stdin.readline().split()))
    if h[2] % h[0] == 0: 
        room1 = h[0]
        room2 = h[2] // h[0]
    else:
        room1 = h[2] % h[0]
        room2 = h[2] // h[0] + 1
    answer  = str(room1)
    if room2 < 10:
        answer += '0'
    answer += str(room2)
    print(answer)
