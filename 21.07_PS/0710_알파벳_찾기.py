x = input()
alpha_dic = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

for i in range(len(x)):
    if alpha_dic[ord(x[i]) - ord('a')] == -1:
        alpha_dic[ord(x[i]) - ord('a')] = i

print(' '.join(map(str, alpha_dic)))
