import sys

# on : 1, off : 0
input = sys.stdin.readline
n = int(input())
switch = [0] + list(map(int, input().split()))
m = int(input())

def man(num):
    for i in range(1, n + 1):
        if i % num == 0:
            switch[i] = not switch[i]
    return

def woman(num):
    i, j = num - 1, num + 1
    switch[num] = not switch[num]
    while True:
        if i < 1 or j > n: break
        if switch[i] != switch[j]: break
        else: switch[i], switch[j] = not switch[i], not switch[j]
        i, j = i - 1, j + 1
    return

for _ in range(m):
    gender, num = map(int, input().split())
    if gender == 1: man(num)
    else: woman(num)

for i in range(1, n + 1):
    print(int(switch[i]), end = ' ')
    if i % 20 == 0: print()
