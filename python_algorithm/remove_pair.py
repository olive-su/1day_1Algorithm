def solution(s):
    s_list = [s[0]]
    for i in range(1, len(s)):
        if len(s_list) > 0 and s_list[-1] == s[i]:
            s_list.pop()
        else:
            s_list.append(s[i])
    if len(s_list) == 0:
        return 1
    return 0
