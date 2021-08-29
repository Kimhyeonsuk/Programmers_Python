import sys
import heapq
def main():
    t=int(sys.stdin.readline())
    for _ in range(t):
        n,m=map(int,sys.stdin.readline().split())
        board=[[]for _ in range(n+1)]
        for _ in range(m):
            a,b,c=map(int,sys.stdin.readline().split())
            board[a].append((b,c))
            board[b].append((a,c))
        k=int(sys.stdin.readline())
        friend=list(map(int,sys.stdin.readline().split()))


        allValue=[0 for _ in range(n+1)]
        for friendNum in friend:
            dist=[1e9 for _ in range(n+1)]
            dist[friendNum]=0
            pq=[(0,friendNum)]
            while pq:
                val=heapq.heappop(pq)
                here=val[1]
                cost=val[0]
                for nextval in board[here]:
                    if dist[nextval[0]]>cost+nextval[1]:
                        dist[nextval[0]]=cost+nextval[1]
                        heapq.heappush(pq,(cost+nextval[1],nextval[0]))
            for i in range(1,n+1):
                allValue[i]+=dist[i]

        resval=1e9
        resRoomNum=0
        for i in range(1,n+1):
            if allValue[i]<resval:
                resval=allValue[i]
                resRoomNum=i
        print(resRoomNum)



