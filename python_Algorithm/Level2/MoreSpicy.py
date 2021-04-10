import heapq
def solution(scoville, K):
    answer = 0
    pq=[]
    for s in scoville:
        heapq.heappush(pq,s)
    while min(pq)<K and len(pq)>=2:
        a=heapq.heappop(pq)
        b=heapq.heappop(pq)
        heapq.heappush(pq,a+b*2)
        answer+=1
    if min(pq)<K:
        answer=-1
    return answer