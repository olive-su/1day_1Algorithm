from sys import stdin
N = int(stdin.readline())
arr = []
cnt = 0
for _ in range(N):
    arr.append(int(stdin.readline()))
arr.sort(reverse=True) # pop()을 이용하기 위해 역순으로 정렬
while len(arr) >= 2:
    sum_val = arr.pop() + arr.pop()
    cnt += sum_val
    for i in range(len(arr)-1, -1, -1):
        if sum_val <= arr[i]:
            arr.insert(i+1, sum_val)
            break
        elif i == 0:
            arr.insert(0, sum_val)
print(cnt)
