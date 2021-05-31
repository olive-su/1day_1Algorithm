input_num = int(input())
cnt = 0
flag = 1
for j in range(1, input_num):
  sequence = list(map(int, str(j)))
  for i in range(1, len(sequence) - 1):
    diff = sequence[0] - sequence[1]
    if diff == (sequence[i - 1] - sequence[i]):
      flag = 0
      break
    flag = 1
  if flag: cnt += 1 
print(cnt)
