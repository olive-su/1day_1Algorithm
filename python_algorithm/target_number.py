def dfs(numbers, target, idx, rst):
    if idx == len(numbers):
        if rst == target:
            return 1
        return 0
    else:
        return dfs(numbers, target, idx+1, rst+numbers[idx]) + dfs(numbers, target, idx+1, rst-numbers[idx])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)
