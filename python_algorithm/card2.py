from collections import deque
a, n = [], int(input())
for i in range(n): a.append(i+1)
a = deque(a)
while len(a) > 1:
    a.popleft()
    a.append(a.popleft())
print(a[0])
