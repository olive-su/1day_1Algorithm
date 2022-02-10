from sys import stdin
n, m = map(int, stdin.readline().split())
attack, _attack = [], []
for _ in range(n):
    r = stdin.readline().split()
    name, val = r[0], int(r[1])
    attack.append((name, val))
attack.sort(key=lambda x: x[1])
_attack.append(attack[0])
for i in range(1, n):
    if attack[i - 1][1] != attack[i][1]:
        _attack.append(attack[i])
for _ in range(m):
    target = int(stdin.readline())
    start, end = 0, len(_attack) - 1
    while start <= end:  # 범위 좁혀갑
        mid = (start + end) // 2
        if _attack[mid][1] == target:
            name = _attack[mid][0]
            break
        elif _attack[mid][1] < target:
            start = mid + 1
            name = _attack[start][0]
        else:
            end = mid - 1
            name = _attack[mid][0]
    print(name)
