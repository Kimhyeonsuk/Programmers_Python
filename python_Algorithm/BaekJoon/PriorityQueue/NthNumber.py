import sys
import heapq
def main():
    pq=[]
    n=int(sys.stdin.readline())
    for _ in range(n):
        nums=list(map(int,sys.stdin.readline().split()))
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq)>n:
                heapq.heappop(pq)
    val=heapq.heappop(pq)
    print(val)