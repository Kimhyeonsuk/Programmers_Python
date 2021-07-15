import sys
import heapq
def main():
    n=int(sys.stdin.readline())
    m=int(sys.stdin.readline())
    bus=[dict() for _ in range(n+1)]
    for _ in range(m):
        a,b,c=map(int,sys.stdin.readline().split())
        if b in bus[a]:
            if bus[a][b]>c:
                bus[a][b]=c
        else:
            bus[a][b]=c
    s,d=map(int,sys.stdin.readline().split())
    dist=[(1e9,0) for _ in range(n+1)]
    dist[s]=(0,0)
    q=[(0,s)]
    while q:
        val=heapq.heappop(q)
        here=val[1]
        cost=val[0]
        for nextloc in bus[here].keys():
            nextcost=bus[here][nextloc]
            if dist[nextloc][0]>nextcost+cost:
                dist[nextloc]=(nextcost+cost,here)
                heapq.heappush(q,(nextcost+cost,nextloc))
    print(dist[d][0])

    loc=d
    arr=[d]
    while True:
        if dist[loc][1]==0:
            break
        else:
            loc=dist[loc][1]
            arr.append(loc)
    print(len(arr))
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end=' ')



