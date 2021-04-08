answer=0
def permutation(cnt,sum,numbers,target):
    if cnt==len(numbers):
        if sum==target:
            global answer
            answer+=1
    else:
        permutation(cnt+1,sum-numbers[cnt],numbers,target)
        permutation(cnt+1,sum+numbers[cnt],numbers,target)
def solution(numbers, target):
    global answer
    numlist=[]
    permutation(0,0,numbers,target)
    return answer