def trapping_rain(buildings):
    for idx in len(buildings)-1:
        if buildings[idx] == 0:
            continue
            

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
