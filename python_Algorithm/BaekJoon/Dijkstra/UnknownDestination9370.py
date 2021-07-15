import sys
import heapq
from collections import defaultdict
def dijkstra(start,edge):
    pq=[(0,start)]
    dist = [1e9 for _ in range(len(edge))]
    dist[start]=0
    while pq:
        val=heapq.heappop(pq)
        here=val[1]
        hereCost=val[0]
        for nextval in edge[here]:
            nextloc=nextval[0]
            cost=nextval[1]
            if dist[nextloc]>hereCost+cost:
                dist[nextloc]=hereCost+cost
                heapq.heappush(pq,(dist[nextloc],nextloc))
    return dist
def solve():
    n,m,t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    edge = [[]for _ in range(n+1)]
    candidate = []
    res=[]
    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        edge[a].append((b,d))
        edge[b].append((a,d))
    for i in range(t):
        x = int(sys.stdin.readline())
        candidate.append(x)

    startDist=dijkstra(s,edge)
    gDist=dijkstra(g,edge)
    hDist=dijkstra(h,edge)

    for candidateNum in candidate:
        if startDist[candidateNum]==startDist[g]+gDist[h]+hDist[candidateNum] or startDist[candidateNum]==startDist[h]+hDist[g]+gDist[candidateNum]:
            res.append(candidateNum)
    res.sort()
    for resNum in res:
        print(resNum,end=' ')
    print('')
def main():
    tc=int(sys.stdin.readline())
    while tc!=0:
        solve()
        tc-=1

