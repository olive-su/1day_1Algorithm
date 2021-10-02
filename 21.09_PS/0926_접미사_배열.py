n = input()
arr = []
for i in range(len(n)):
    arr.append(n[i:])
arr.sort()
for j in arr:
    print(j)
