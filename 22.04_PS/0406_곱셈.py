def divide_and_conquer(a, b):
    if b == 1:
        return a % c

    rst = divide_and_conquer(a, b // 2)
    
    if b % 2 == 0:
        return rst * rst % c
    else:
    	return rst * rst * a % c
        
        
a, b, c = map(int, input().split())

print(divide_and_conquer(a, b))