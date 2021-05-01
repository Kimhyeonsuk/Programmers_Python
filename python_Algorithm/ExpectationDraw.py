def solution(n,a,b):
    answer = 3
    tmp=2
    cnt=0
    for i in range(1,21):
        if tmp==n:
            cnt=i
            break
        else:
            tmp=tmp*2
    while n!=0:
        n=n//2
        if (a-1)//n!=(b-1)//n:
            answer=cnt
            break
        else:
            cnt-=1
    return answer