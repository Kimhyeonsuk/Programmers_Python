import sys
import heapq
def solution(n,list):
    pq=[]
    res=[]
    input=[0 for _ in range(n+1)]
    board=[[] for _ in range(n+1)]
    for val in list:
        s=val[0]
        d=val[1]
        input[d]+=1
        board[s].append(d)
    for i in range(1,n+1):
        if input[i]==0:
            heapq.heappush(pq,i)

    while pq:
        val=heapq.heappop(pq)
        res.append(val)
        for next in board[val]:
            input[next]-=1
            if input[next]==0:
                heapq.heappush(pq,next)

    return res


n,m=tuple(map(int,sys.stdin.readline().split()))
l=[]
for i in range(m):
    val=tuple(map(int,sys.stdin.readline().split()))
    l.append(val)
res=solution(n,l)
for num in res:
    print(num,end=" ")