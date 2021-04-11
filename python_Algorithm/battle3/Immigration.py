def canImmigrate(mid,times,n):
    res=0
    for time in times:
        res+=int(mid/time)
    if res>=n:
        return True
    else:
        return False
def solution(n, times):
    answer = 0
    times.sort()
    low=0
    high=n*times[-1]

    while low<=high:
        mid=int((low+high)/2)

        if canImmigrate(mid,times,n):
            high=mid-1
        else:
            low=mid+1
    return low