def solution(nums):
    answer = 0
    numset=set(nums)
    n=int(len(nums)/2)
    if len(numset)<=n:
        answer=len(numset)
    else:
        answer=n
    return answer