# boj. 14891
# time: 30

import sys
input = sys.stdin.readline
wheels, order = [], []
for _ in range(4):
    wheels.append(list(input().rstrip()))
for _ in range(int(input())):
    order.append(tuple(map(int, input().split())))

def right_rotation(wheel):
    t = wheel[-1]
    wheel = wheel[:-1]
    wheel.insert(0, t)
    return wheel

def left_rotation(wheel):
    t = wheel[0]
    wheel = wheel[1:]
    wheel.append(t)
    return wheel

for o, d in order:
    new_wheels = wheels[:]
    if d == 1: new_wheels[o - 1] = right_rotation(wheels[o - 1])
    else: new_wheels[o - 1] = left_rotation(wheels[o - 1])
    r = d
    for i in range(o - 1, 0, -1):
        if wheels[i][6] != wheels[i - 1][2]:
            if r == 1: new_wheels[i - 1] = left_rotation(wheels[i - 1])
            elif r == -1: new_wheels[i - 1] = right_rotation(wheels[i - 1])
            else: break
            r = -r
        else: r = 0
    r = d
    for i in range(o - 1, 3):
        if wheels[i][2] != wheels[i + 1][6]:
            if r == 1: new_wheels[i + 1] = left_rotation(wheels[i + 1])
            elif r == -1: new_wheels[i + 1] = right_rotation(wheels[i + 1])
            else: break
            r = -r
        else: r = 0
    wheels = new_wheels

answer = 0
for i in range(4):
    answer += 2 ** i * int(wheels[i][0])

print(answer)

