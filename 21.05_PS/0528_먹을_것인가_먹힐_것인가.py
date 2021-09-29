def binary_search(element, some_list):
    start, end = 0, len(some_list)-1
    result = -1
    while start <= end:
        middle = (start + end) // 2
        if some_list[middle] < element:
            result = middle
            start = middle + 1
        else:
            end = middle - 1
    return result

repeat = int(input())
for i in range(repeat):
  count = 0
  a, b = map(int, input().split())
  groupA = list(map(int,input().split()))
  groupB = list(map(int,input().split()))
  groupA.sort()
  groupB.sort()
  for l in groupA:
    count += (binary_search(l, groupB) + 1)
  print(count)
