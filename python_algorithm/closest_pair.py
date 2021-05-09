from math import sqrt

def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

def closest_pair(coordinates):
    optimal_destination = [coordinates[0], coordinates[1]]
    for i in range(len(coordinates)-1):
        for j in range(i + 1, len(coordinates)):
            if distance(optimal_destination[0], optimal_destination[1]) > distance(coordinates[i], coordinates[j]):
                optimal_destination = [coordinates[i], coordinates[j]]
    return optimal_destination

test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
