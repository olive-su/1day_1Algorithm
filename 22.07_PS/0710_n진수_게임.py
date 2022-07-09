def num(n, num):
    arr = '0123456789ABCDEF'
    rst = []
    rst.append(arr[num % n])
    while num >= n:
        num //= n
        rst.append(arr[num % n])
    rst.reverse()
    return rst
    

def solution(n, t, m, p):
    answer = ''
    arr = [0]
    for i in range(t * m):
        arr += num(n, i)
    now = p
    while len(answer) < t:
        answer += arr[now]
        now += m
    return answer