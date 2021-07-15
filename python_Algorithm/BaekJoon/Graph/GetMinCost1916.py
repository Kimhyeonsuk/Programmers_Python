import sys
import heapq
def main():
    global n,m,bus,s,d
    n=int(sys.stdin.readline())
    m=int(sys.stdin.readline())
    bus=[dict() for _ in range(n+1)]

    for _ in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        if b in bus[a] :
            if bus[a][b]>c:
                bus[a][b]=c
        else:
            bus[a][b]=c
    s,d=map(int,sys.stdin.readline().split())
    dist=[1e9 for _ in range(n+1)]
    dist[s]=0

    q=[(0,s)]

    while q:
        val=heapq.heappop(q)
        cost=val[0]
        here=val[1]
        for items in bus[here].keys():
            nextval=bus[here][items]
            nextloc=items
            nextcost=nextval
            if dist[nextloc]>cost+nextcost:
                dist[nextloc]=cost+nextcost
                heapq.heappush(q,(cost+nextcost,nextloc))
    print(dist[d])
