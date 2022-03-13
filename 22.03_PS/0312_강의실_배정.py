from sys import stdin
t = int(stdin.readline())
rooms = {}
for _ in range(t):
    start, end = map(int, stdin.readline().split())
    flag = 1
    for i in range(len(rooms)):
        if start in rooms[str(i)] or (end - 1) in rooms[str(i)]:
            continue
        else:
            flag = 0
    if flag:
        rooms[str(len(rooms))] = [i for i in range(start, end)]
print(len(rooms))
