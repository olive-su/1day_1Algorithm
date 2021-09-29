keyList = list(map(int, input().split()))
keyList.sort()
for i in range(1, keyList[0] + 1):
  if ((keyList[0] % i == 0) and (keyList[1] % i == 0)and (keyList[2] % i == 0)):
    maximum = i
print(maximum)
