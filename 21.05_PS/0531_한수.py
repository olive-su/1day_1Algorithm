input_num = int(input())
cnt = 0
flag = 1
for j in range(1, input_num + 1):
  sequence = list(map(int, str(j)))
  for i in range(2, len(sequence)):
    diff = sequence[0] - sequence[1]
    flag = 1
    if diff != (sequence[i - 1] - sequence[i]):
      flag = 0
      break
  if flag: cnt += 1 
print(cnt)
