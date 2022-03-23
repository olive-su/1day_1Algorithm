from sys import stdin
n = int(stdin.readline())
d = [0] * n
arr = []
arr.append(int(stdin.readline()))
d[0] = arr[-1]
if n >= 2:
    arr.append(int(stdin.readline()))
    d[1] = d[0] + arr[-1]
    if n >= 3:
        arr.append(int(stdin.readline()))
        d[2] = max(arr[1] + arr[-1], arr[0] + arr[-1])
        for i in range(3, n):
            num = int(stdin.readline())
            md1 = max(d[:i-1])
            md2 = max(d[:i-2])
            d[i] = max(md1 + num, md2 + arr[-1] + num)
            arr.append(num)
print(max(d))

