import sys

while True:
    try:
        hole = int(sys.stdin.readline().rstrip()) * 10000000
        n = int(sys.stdin.readline().rstrip())
        block = []
        flag, start, end = 1, 0, n-1
        for _ in range(n):
            block.append(int(sys.stdin.readline().rstrip()))
        block.sort()
        while start < end:
            if hole == block[start] + block[end]:
                print("yes {} {}".format(block[start], block[end]))
                flag = 0
                break
            elif hole < block[start] + block[end]:
                end -= 1
            else:
                start += 1
        if flag: print("danger")
    except:
        break
