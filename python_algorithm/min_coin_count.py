def min_coin_count(value, coin_list):
    count = 0
    coin_list = sorted(coin_list, reverse=True)
    for i in range(0, len(coin_list)):
        if (value == 0):
            return count
        elif (value >= coin_list[i]):
            count += (value // coin_list[i])
            value -= ((value // coin_list[i]) * coin_list[i])
    return count

default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
