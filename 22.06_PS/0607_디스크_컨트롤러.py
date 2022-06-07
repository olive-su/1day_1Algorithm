# 프로그래머스 힙

def solution(jobs):
    jobs.sort()
    jobs.sort(key = lambda x : x[1])
    
    n = len(jobs)
    answer = 0
    now = 0
    while len(jobs) > 0:
        time = 1
        process = None
        for i, j in jobs:
            if i <= now and time == 1:
                time = 0
                process = [i, j]
        if process != None:
            now += process[1]
            answer += (now - process[0])
            jobs.remove(process)
        else:
            now += 1
        
    return answer // n