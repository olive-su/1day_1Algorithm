import sys

input = sys.stdin.readline
bracket = input().rstrip()
s, b = 0, 0 # 소괄호, 대괄호
dp = [[] for _ in range(31)]
stack = []
weight = {'(':2, '[':3, ']':3, ')':2}

def cnt(inputs, s, b): # 괄호 개수 확인 함수
    if inputs == '(': s += 1
    elif inputs == '[': b += 1
    elif inputs == ')': s -= 1
    else: b -= 1
    return s, b

for i in range(len(bracket)):
    target = bracket[i]
    s, b = cnt(target, s, b)
    if s == -1 or b == -1:
        sys.exit(print(0))
    if target == '(' or target == '[':
        stack.append(weight[target])
    else:
        v = stack.pop()
        if weight[target] != v: # 괄호 순서를 위한 선입후출 -> [(]) 이 경우 처리를 위함
            sys.exit(print(0))
        if len(dp[len(stack) + 1]): # 스택의 상위 랭크에 인자가 있는 경우
            rst = int(v) * sum(dp[len(stack) + 1])
            dp[len(stack) + 1] = []
        else:
            rst = int(v)
        dp[len(stack)].append(rst)
if s or b:
    print(0)
else:
    print(sum(dp[0]))