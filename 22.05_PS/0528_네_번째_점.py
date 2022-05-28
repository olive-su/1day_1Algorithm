import sys

input = sys.stdin.readline
x_set, y_set = [], []
for _ in range(3):
    x, y = map(int, input().split())
    if x in x_set: x_set.remove(x)
    else: x_set.append(x)
    if y in y_set: y_set.remove(y)
    else: y_set.append(y)

print(x_set[0], y_set[0])