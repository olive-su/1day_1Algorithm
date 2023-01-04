#boj. 11653
#time : 20'

from math import sqrt

MAX_NUM = int(1e7)
n = int(input())
s = 2

is_prime = [True] * (MAX_NUM + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2,  int(sqrt(MAX_NUM)) + 1):
    num = 2
    if is_prime[i]: # True
        while num * i <= MAX_NUM:
            is_prime[num * i] = False
            num += 1

if n < s: exit()
while n > 1:
    if n % s == 0:
        n //= s
        print(s)
    else:
        s += 1
        while not is_prime[s]: #False
            s += 1

