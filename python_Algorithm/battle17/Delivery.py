import heapq
def solution(N, road, K):
    answer = 0
    dist=[1e9 for i in range(N+1)]
    maplist=[dict([]) for i in range(N+1)]
    for roadinfo in road:
        s=roadinfo[0]
        d=roadinfo[1]
        val=roadinfo[2]
        if d in maplist[s]:
            if maplist[s][d]>val:
                maplist[s][d] = val
        else:
            maplist[s][d]=val
        if s in maplist[d]:
            if maplist[d][s]>val:
                maplist[d][s]=val
        else:
            maplist[d][s]=val
    dist[1]=0
    q=[]
    heapq.heappush(q,(0,1))
    while q:
        val=heapq.heappop(q)
        here=val[1]
        cost=val[0]
        for nextNum,value in maplist[here].items():
            if dist[nextNum]>cost+value:
                dist[nextNum]=cost+value
                heapq.heappush(q,(cost+value,nextNum))

    for i in range(1,N+1):
        if dist[i]<=K:
            answer+=1
    return answer