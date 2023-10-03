c = input()

t = ''
visited = [False] * len(c)

while len(t) < len(c):
    max_score = 'Z' * 100
    max_target = 0
    now, t = '', ''

    for i in range(len(c)):
        if visited[i]:
            now += c[i]
            continue

        if not visited[i]:
            tmp = now + c[i]
            for j in range(i + 1, len(c)):
                if visited[j]:
                    tmp += c[j]

            if tmp < max_score:
                max_score = tmp
                max_target = i
    visited[max_target] = True
    for i in range(len(c)):
        if visited[i]:
            t += c[i]
    print(t)
