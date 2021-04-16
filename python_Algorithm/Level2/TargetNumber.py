answer=0
def permutation(cnt,number,sum,target):
    if cnt==len(number):
        if sum==target:
            global answer
            answer+=1
        return
    permutation(cnt+1,number,sum+number[cnt],target)
    permutation(cnt+1,number,sum-number[cnt],target)

def solution(number,target):
    global answer
    permutation(0,number,0,target)
    return answer