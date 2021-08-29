import sys
import heapq
def main():
    n=int(sys.stdin.readline())
    info=[]
    for _ in range(n):
        s,t=map(int,sys.stdin.readline().split())
        info.append((s,t))
    info.sort(key=lambda x:(x[0],x[1]))
    res=0
    pq=[]
    for val in info:
        if not pq:
            heapq.heappush(pq,val[1])
            res+=1
        else:
            if pq[0]>val[0]:
                res+=1
                heapq.heappush(pq, val[1])
            else:
                heapq.heappop(pq)
                heapq.heappush(pq,val[1])
    print(res)


