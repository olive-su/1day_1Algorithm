from collections import Counter

x = int(input())
i, num = 1, 0
while True:
    string = str(i)
    counter = Counter(string)
    if '666' in string:
        num += 1
    if num == x:
        break
    i += 1
print(string)
