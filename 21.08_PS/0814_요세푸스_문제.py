a, b = input().split()
a, b = int(a), int(b)
n, k = [i for i in range(1, a + 1)], []
c = b
while n:
    while c > len(n):
        c -= len(n)
    k.append(n.pop(c-1))
    c += b - 1
k = list(map(str, k))
print('<'+', '.join(k)+'>')


