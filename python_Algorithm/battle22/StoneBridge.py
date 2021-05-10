def chk(rocks,n,mid,dist):
    cnt=0
    here=0
    for num in rocks:
        if num-here<mid:
            cnt+=1
        else:
            here=num
    if dist-here<mid:
        cnt+=1

    if cnt>n:
        return True
    else:
        return False



def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    low=0
    high=distance
    while low<high:
        mid=(low+high)//2
        if chk(rocks,n,mid,distance):
            high=mid-1
        else:
            low=mid+1

    return low