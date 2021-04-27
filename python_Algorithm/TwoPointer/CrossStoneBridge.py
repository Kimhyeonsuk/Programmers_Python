def chk (stones,mid):
    cnt=0
    res=0
    for stone in stones:
        if stone<mid:
            res=max(res,cnt)
            cnt=0
        else:
            cnt+=1

    if mid>res:
        return False
    else:
        return True
def solution(stones, k):
    answer = 0
    low=0
    high=max(stones)
    while low<=high :
        mid=(low+high)//2
        if chk(stones,mid):
            low=mid+1
        else:
            high=mid-1

    return low