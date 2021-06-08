import sys
def main():
    n,m=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    start=0
    end=0
    res=0
    sum=arr[0]
    while start<n and end<n:
        if sum==m:
            res+=1
            sum-=arr[start]
            start+=1
            end+=1
            if end<n:
                sum+=arr[end]
        elif sum<m:
            end+=1
            if end<n:
                sum+=arr[end]
        elif sum>m:
            sum-=arr[start]
            start += 1
    print(res)