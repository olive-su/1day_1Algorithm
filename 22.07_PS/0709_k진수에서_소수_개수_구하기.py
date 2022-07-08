import math

# 에라토스테네스 풀이
# 테스트케이스 1, 11 불통
# def is_prime(n):
    # arr = [True] * (n + 1)
    # arr[0], arr[1] = False, False
    # for i in range(2, int(math.sqrt(n)) + 1):
    #     num = 2
    #     if arr[i] == True:
    #         while i * num <= n:
    #             arr[i * num] = False
    #             num += 1
    # return arr[n]

def is_prime(n):
    num = 2
    if n < 2: return False
    while num < int(math.sqrt(n)) + 1:
        if n % num == 0:
            return False
        num += 1
    return True

def num(k, n):
    rst = [str(n % k)]
    while n >= k:
        n //= k
        rst.append(str(n % k))
    rst.reverse()
    return ''.join(rst)


def solution(n, k):
    answer = 0
    arr = num(k, n).split('0')
    for a in arr:
        if a != '' and is_prime(int(a)):
            answer += 1
    return answer