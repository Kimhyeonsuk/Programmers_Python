import sys
import heapq
def main():
    n,k=map(int,sys.stdin.readline().split())
    gemInfo=[]
    clist=[]
    for i in range(n):
        m=list(map(int,sys.stdin.readline().split()))
        heapq.heappush(gemInfo,m)
    for i in range(k):
        c=int(sys.stdin.readline())
        clist.append(c)
    clist.sort()
    res=0
    pq=[]
    for cval in clist:
        while gemInfo and gemInfo[0][0]<=cval:
            heapq.heappush(pq,-heapq.heappop(gemInfo)[1])
        if pq:
            res-=heapq.heappop(pq)

    print(res)

