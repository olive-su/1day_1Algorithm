def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1,cache) + fib_memo(n - 2,cache)
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)
