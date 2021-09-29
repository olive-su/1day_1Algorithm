def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                answer.append(j - i)
                break
            if j == len(prices) - 1:
                answer.append(len(prices) - 1 - i)
    answer.append(0)
    
    return answer
