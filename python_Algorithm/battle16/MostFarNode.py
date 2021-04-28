def BFS(n,maplist,chk):
    q=[]
    q.append((1,0))
    chk[1]=True
    EdgeNum=[0 for i in range(n+1)]
    EdgeNum[1]=0
    maxEdge=0
    while q:
        here=q.pop(0)
        for nextnum in maplist[here[0]]:
            if not chk[nextnum]:
                chk[nextnum]=True
                q.append((nextnum,here[1]+1))
                EdgeNum[nextnum]=here[1]+1
                maxEdge=max(maxEdge,here[1]+1)
    res=0
    for i in range(1,n+1):
        if EdgeNum[i]==maxEdge:
            res+=1
    return res

def solution(n, edge):
    answer = 0
    maplist=[[] for i in range(n+1)]
    chk=[False for i in range(n+1)]
    for edgeinfo in edge:
        s=edgeinfo[0]
        d=edgeinfo[1]
        maplist[s].append(d)
        maplist[d].append(s)


    return BFS(n,maplist,chk)