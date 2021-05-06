def fib(n):
    if (n < 3):
        return 1
    else:
        return fib(n-2) + fib(n-1)

# Test
for i in range(1, 11):
    print(fib(i))
