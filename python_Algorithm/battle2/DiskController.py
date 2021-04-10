import queue
import collections
def solution(jobs):
    answer = 0
    length=len(jobs)
    jobs=list(jobs)
    jobs.sort()
    q=collections.deque()
    jq=[]
    sec=0
    while jobs or q:
        if jobs and jobs[0][0]<=sec:
            q.append(jobs.pop(0))
            continue
        if q:
            q=collections.deque(sorted(q,key=lambda x:x[1]))
            val=q.popleft()
            sec+=val[1]
            answer+=sec-val[0]
        else:
            sec+=1
    return int(answer/length)