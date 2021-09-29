N = int(input())
if N == 1: 
    print(1)
    exit(0)
i = 0
while N - 1 > 0:
    N -= (i * 6)
    i+=1
print(i)
