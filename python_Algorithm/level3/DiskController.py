import heapq
def solution(jobs):
    answer = 0
    waitingq=[]
    sec=0
    n=len(jobs)
    jobs.sort(key=lambda x:x[0])
    while jobs or waitingq:
        if jobs:
            while jobs and jobs[0][0]<=sec:
                val=jobs.pop(0)
                heapq.heappush(waitingq,(val[1],val[0]))
        if waitingq:
            val=heapq.heappop(waitingq)
            sec+=val[0]
            answer+=sec-val[1]
        else:
            sec+=1
    return answer//n