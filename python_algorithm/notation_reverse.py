def solution(n):
    list_n = []
    while (n > 0):
        list_n.append(n % 3)
        n //= 3
    list_n.reverse()
    answer = 0
    for i in range(len(list_n)):
        answer += (3 ** i) * list_n[i]
        
    return answer
