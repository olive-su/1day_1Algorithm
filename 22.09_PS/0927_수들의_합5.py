import sys

input = sys.stdin.readline
n = int(input())
answer, sum = 1, 1
start, end = 1, 1

while(end != n):
    if(sum == n):
        answer += 1
        end += 1
        sum += end
    elif(sum < n):
        end += 1
        sum += end
    else:
        sum -= start
        start += 1

print(answer)