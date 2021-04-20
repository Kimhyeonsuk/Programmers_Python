import heapq
def solution(n, works):
    answer = 0
    maxheap=[]
    for work in works:
        heapq.heappush(maxheap,-work)
    while n!=0:
        val=-(heapq.heappop(maxheap))
        heapq.heappush(maxheap,-(val-1))
        n-=1
    while maxheap:
        val=-heapq.heappop(maxheap)
        if val<0:
            continue
        answer+=pow(val,2)
    return answer