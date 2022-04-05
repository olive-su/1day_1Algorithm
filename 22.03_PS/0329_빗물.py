import sys

input = sys.stdin.readline
h, w = map(int, input().split())
blocks = list(map(int, input().split()))
rst = 0

for i in range(1, h + 1):
    for j in range(1, w - 1):
        if i > blocks[j]:
            if max(blocks[:j]) >= i and max(blocks[j+1:]) >= i:
                rst += 1
print(rst)
