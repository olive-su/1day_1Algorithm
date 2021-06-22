import collections

def solution(nums):
    type_num = len(collections.Counter(nums))
    if type_num < len(nums) // 2:
        return type_num
    else:
        return len(nums) // 2
