import sys
import heapq
def main():
    n,k=map(int,sys.stdin.readline().split())
    customers=[]
    for _ in range(n):
        id,dom=map(int,sys.stdin.readline().split())
        customers.append((id,dom))
    casher=[]
    for i in range(k):
        heapq.heappush(casher,(0,i+1))
    res=[]
    for idx,cusInfo in enumerate(customers):
        casherInfo=heapq.heappop(casher)
        time=casherInfo[0]
        casherNum=casherInfo[1]
        res.append((time+cusInfo[1],-casherNum,idx))
        heapq.heappush(casher,(time+cusInfo[1],casherNum))
    res.sort()
    returnValue=0
    for idx,info in enumerate(res):
        cusId=info[2]
        returnValue+=(idx+1)*customers[cusId][0]
    print(returnValue)



