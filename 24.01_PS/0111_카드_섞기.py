import sys
from itertools import product
import math

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
prod = list(product(range(1, int(math.sqrt(n)) + 1),
            range(1, int(math.sqrt(n)) + 1)))

# 카드 섞기 수행


def shuffle_cards(cards, t):
    if t == -1:
        return cards

    up = int(math.pow(2, t))
    cards = shuffle_cards(cards[len(cards) - up:],
                          t - 1) + cards[:len(cards) - up]
    return cards


# k 범위로 부터 나올 수 있는 중복 순열 리스트를 순회하며 카드 섞기 수행
for p in prod:
    origin = list(range(1, n + 1))  # 원본 리스트 (1 to n)

    a, b = p
    output = shuffle_cards(shuffle_cards(origin, a), b)  # 카드 2번 섞기 수행

    if output == cards:
        print(p[0], p[1], sep=' ')
        break
