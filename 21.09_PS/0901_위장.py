def solution(clothes):
    clothes_category = {}
    answer = 1
    for c in clothes:
        if c[1] in clothes_category.keys():
            clothes_category[c[1]] += 1
        else:
            clothes_category[c[1]] = 2
    for a in clothes_category.items():
        answer *= a[1]
    return answer - 1
