import heapq
import sys
N=int(input())
pq=[]
res=[]
for i in range(N):
    num=int(sys.stdin.readline())
    if num==0:
        if not pq:
            res.append(0)
        else:
            res.append(heapq.heappop(pq))
    else:
        heapq.heappush(pq,num)
for num in res:
    print(num)