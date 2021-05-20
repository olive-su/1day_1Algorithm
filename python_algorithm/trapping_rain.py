def trapping_rain(buildings):
    rain_amount = 0

    for i in range(1, len(buildings) - 1):
        left_height = max(buildings[:i])
        right_height = max(buildings[i:])

        lower_height = min(left_height, right_height)

        rain_amount += max(0, lower_height - buildings[i])

    return rain_amount

print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
