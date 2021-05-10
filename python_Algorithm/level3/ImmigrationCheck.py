def solution(n, times):
    answer = 0
    low=1
    high=max(times)*n
    while low<=high:
        mid=(low+high)//2
        sum=0
        for time in times:
            sum+=mid//time
        if sum<n:
            low=mid+1
        else:
            high=mid-1
    return low