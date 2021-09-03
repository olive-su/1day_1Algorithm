def binary_search(tree, start, end):
    if start > end:
        return print(end)
    length = 0
    mid = (end + start) // 2
    for i in tree:
        if i < mid:
            break
        length += i - mid
    if length >= M:
        binary_search(tree, mid+1, end)
    else:
        binary_search(tree, start, mid-1)


from sys import stdin
N, M = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))
tree.sort(reverse=True)
start, end = 0, tree[0]
binary_search(tree, start, end)
