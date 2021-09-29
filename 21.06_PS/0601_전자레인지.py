input_num = int(input())
list_time = [0, 0, 0]
if input_num >= 300:
  list_time[0] = input_num // 300
  input_num = input_num % 300
if input_num >= 60:
  list_time[1] = input_num // 60
  input_num = input_num % 60
if input_num >= 10:
  list_time[2] = input_num // 10
  input_num = input_num % 10
if input_num:
  print(-1)
else:
  print(list_time[0], list_time[1], list_time[2])
