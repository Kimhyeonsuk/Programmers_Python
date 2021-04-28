import heapq
# 플루이드 와샬을 이용한 풀이, 최대 테스트 케이스 40ms
# def solution(N, road, K):
#     answer = 0
#     dist=[[1e9 for i in range(N+1)]for j in range(N+1)]
#     for i in range(1,N+1):
#         dist[i][i]=0
#     # vector=[[]for i in range(N)]
#     for roadinfo in road:
#         dist[roadinfo[0]][roadinfo[1]]=min(dist[roadinfo[0]][roadinfo[1]],roadinfo[2])
#         dist[roadinfo[1]][roadinfo[0]]=min(dist[roadinfo[1]][roadinfo[0]],roadinfo[2])
#     for k in range(1,N+1):
#         for i in range(1,N+1):
#             for j in range(1,N+1):
#                 dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
#     for i in range(1,N+1):
#         if dist[1][i]<=K:
#             answer+=1
#     return answer
import heapq
# 다익스트라를 이용한 풀이 1.97ms 
def solution(N,road,K):
    answer=0
    q=[]
    dist=[1e9 for i in range(N+1)]
    vector=[dict([]) for i in range(N+1)]
    for roadInfo in road:
        if roadInfo[1] in vector[roadInfo[0]]:
            if vector[roadInfo[0]][roadInfo[1]]>roadInfo[2]:
                vector[roadInfo[0]][roadInfo[1]] = roadInfo[2]
        else:
            vector[roadInfo[0]][roadInfo[1]]=roadInfo[2]

        if roadInfo[0] in vector[roadInfo[1]]:
            if vector[roadInfo[1]][roadInfo[0]]>roadInfo[2]:
                vector[roadInfo[1]][roadInfo[0]] = roadInfo[2]
        else:
            vector[roadInfo[1]][roadInfo[0]]=roadInfo[2]

    heapq.heappush(q,(0,1))
    dist[1]=0
    while q:
        val=heapq.heappop(q)
        cost=val[0]
        here=val[1]
        for nextval in vector[here].keys():
            nextNodeNum=nextval
            nextCost=vector[here][nextval]
            if dist[nextNodeNum]>cost+nextCost:
                dist[nextNodeNum]=cost+nextCost
                heapq.heappush(q,(cost+nextCost,nextNodeNum))
    for i in range(1,N+1):
        if dist[i]<=K:
            answer+=1
    return answer