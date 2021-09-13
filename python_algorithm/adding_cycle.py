import sys
x = int(sys.stdin.readline().rstrip())
cycle, next = 0, x
while True:
    cycle += 1
    digit_sum = (next // 10) + (next % 10)
    next = (next % 10) * 10 + digit_sum % 10
    if next == x: break
print(cycle)
