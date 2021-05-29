round = int(input())
count = 0
long_side = round // 2
for i in range(long_side, 0, -1):
  if i < (round - i)//2:
    break
  if i < (round - i):
    for j in range(1, (round - i)//2 + 1):
      side_1 = j
      side_2 = (round - i - side_1)
      if (i >= side_1) and (i >= side_2):
        count += 1
print(count)
