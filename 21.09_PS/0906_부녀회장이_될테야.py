def living_people(k ,n):
    people = [[] * i for i in range(15)]
    for i in range(k+1):
        for j in range(1, n+1):
            if i == 0:
                people[i].append(j)
            else:
                people[i].append(sum(people[i-1][:j]))
    print(people[k][n-1])


from sys import stdin
for _ in range(int(stdin.readline())):
    k = int(stdin.readline())
    n = int(stdin.readline())
    living_people(k, n)
