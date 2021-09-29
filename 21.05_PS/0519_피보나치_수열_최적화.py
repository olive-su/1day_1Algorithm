def fib_optimized(n):
    current = 1
    previous = 0

    # update
    for i in range(1, n):
        current, previous = current + previous, current

    return current
