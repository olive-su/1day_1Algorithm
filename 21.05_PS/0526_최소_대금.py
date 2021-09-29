pizza =[]
juice = []
for i in range(3):
  pizza.append(float(input()))
for i in range(2):
  juice.append(float(input()))
print(min(pizza) + min(juice) + (min(pizza) + min(juice)) * 0.1)
