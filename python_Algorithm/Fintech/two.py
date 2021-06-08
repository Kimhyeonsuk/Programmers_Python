def solution(endingTime, jobs):
    answer = []
    sec=0
    workingQ=[]
    while True:
        while jobs and jobs[0][1]<=sec:
            workingQ.append(jobs.pop(0))
        if workingQ :
            val=workingQ.pop()
            sec+=val[3]
            if sec<=val[2] and sec<=endingTime:
                answer.append(val[0])
        else:
            sec+=1
        if (not workingQ and not jobs) or sec>endingTime:
            break
    return answer