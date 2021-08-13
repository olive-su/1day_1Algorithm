def factorial(n):
    a = 1
    for i in range(2, n+1):
        a *= i
    return a

n, k = input().split()
n, k = int(n), int(k)
print(factorial(n)//(factorial(n-k)*factorial(k)))
