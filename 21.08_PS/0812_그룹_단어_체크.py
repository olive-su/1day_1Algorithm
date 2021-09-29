cnt = 0
n = int(input())
for _ in range(n):
    s = input()
    m = s[0]
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            m += s[i]
    if len(set(s)) == len(m): cnt+=1
print(cnt)
