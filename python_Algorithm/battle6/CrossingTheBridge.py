def chk(stones,mid):
    res=0
    cnt=0
    for num in stones:
        if num<=mid:
            cnt+=1
        else:
            res=max(res,cnt)
            cnt = 0
    return max(res,cnt)
def solution(stones, k):
    answer = 1e9
    high=max(stones)
    low=1

    while(low<=high):
        mid=int((low+high)/2)
        a=chk(stones,mid)
        if a<k:
            low=mid+1
        else:
            high=mid-1

    return low