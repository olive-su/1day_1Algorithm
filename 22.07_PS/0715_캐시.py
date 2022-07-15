# programmers

from collections import defaultdict

def change(cacheSize, stack, dict):
    items = list(dict.items())
    items.sort(key = lambda x : x[1], reverse=True) # 인덱스 큰 순서대로 정렬
    a, b = items[cacheSize - 1]
    stack.remove(a)
    dict[a] = -1
    return stack, dict

def solution(cacheSize, cities):
    answer = 0
    stack = []
    time = defaultdict(int)
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for c in range(len(cities)):
        name = cities[c].upper()
        if name in stack:
            time[name] = c
            answer += 1
        else:
            if len(stack) < cacheSize:
                stack.append(name)
                time[name] = c
                answer += 5
            else:
                stack, time = change(cacheSize, stack, time)
                stack.append(name)
                time[name] = c
                answer += 5
    
    return answer