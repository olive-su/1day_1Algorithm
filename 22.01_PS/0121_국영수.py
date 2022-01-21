from sys import stdin
N = int(stdin.readline())
students = [] # 학생 명단
for _ in range(N):
    students.append(stdin.readline().split())

students.sort(key=lambda x : x[0])
students.sort(key=lambda x : int(x[3]), reverse=True)
students.sort(key=lambda x : int(x[2]))
students.sort(key=lambda x : int(x[1]), reverse=True)

[print(students[i][0]) for i in range(N)]
