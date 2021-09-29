# 가장 가격이 싼 주유소면 맨 끝까지 갈 수 있는 양 주유
# 그게 아니라면 지금 주유소랑 가장 가까우면서 가격이 낮은 곳 탐색후 거기까지 이동

from sys import stdin
n = int(stdin.readline())
distance = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
cheap_price = min(price)
money, now_price = 0, 1000000000
for i in range(n-1):
    if price[i] < now_price:
        now_price = price[i]
    money += now_price * distance[i]
print(money)
