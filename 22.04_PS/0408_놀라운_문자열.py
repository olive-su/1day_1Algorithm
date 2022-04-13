import sys

input = sys.stdin.readline

suprising = input().rstrip()
while suprising != "*":
    arr = [[] for _ in range(len(suprising))]
    flag = 0
    for i in range(1, len(suprising)):
        for j in range(i, len(suprising)):
            new = suprising[j - i] + suprising[j]
            if new in arr[i]:
                flag = 1
            arr[i].append(new)
    if flag :
        print(suprising, "is NOT surprising.")
    else:
        print(suprising, "is surprising.")
    suprising = input().rstrip()
