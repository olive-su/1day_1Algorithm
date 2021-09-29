from sys import stdin
n = int(stdin.readline())
a = []
for _ in range(n):
    a.append(int(stdin.readline()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    small, middle, big =[], [], []
    for i in arr:
        if i < pivot:
            small.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            big.append(i)
    arr = quick_sort(small) + middle + quick_sort(big)
    return arr

a = quick_sort(a)
print('\n'.join(list(map(str, a))))
