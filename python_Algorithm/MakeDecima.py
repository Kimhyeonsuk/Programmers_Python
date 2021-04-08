import math
ans=[0]
def chkDecimal(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def permutation(idx,list,nums):
    if len(list)==3:
        if chkDecimal(sum(list)):
            ans[0]+=1
    else:
        for i in range(idx,len(nums)):
            list.append(nums[i])
            permutation(i+1,list,nums)
            list.pop()
def solution(nums):
    answer = -1
    list=[]
    permutation(0,list,nums)
    return ans[0]
