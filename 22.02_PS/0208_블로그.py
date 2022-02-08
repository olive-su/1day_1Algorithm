from sys import stdin
n, x = map(int, stdin.readline().split())
visiter = list(map(int, stdin.readline().split()))
_sum = sum(visiter[:x])
_max = _sum
cnt = 1
for i in range(n - x):
    _sum -= visiter[i]
    _sum += visiter[i + x]
    if _sum > _max:
        cnt = 1
        _max = _sum
    elif _sum == _max:
        cnt += 1

print(_max, cnt, sep='\n') if _sum != 0 else print("SAD")
