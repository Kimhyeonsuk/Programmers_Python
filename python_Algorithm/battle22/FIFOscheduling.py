def solution(n, cores):
    answer = 0
    low=0
    high=max(cores)*n
    while low<=high:
        mid=(low+high)//2

        sum=0
        for core in cores:
            sum+=mid//core
        if sum>n:
            high=mid-1
        else:
            low=mid+1
    for idx,core in enumerate(cores):
        if low%core==0:
            answer=idx+1
    return answer