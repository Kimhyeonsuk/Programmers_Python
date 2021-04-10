def solution(n):
    answer=[]
    res= [[0 for n in range(i)] for i in range(1,n+1)]
    num=0
    cnt=0
    loc=[-1,0]
    while n!=0:
        for i in range(0,n):
            num+=1
            if cnt==0:
                loc=[loc[0]+1,loc[1]]
                res[loc[0]][loc[1]]=num
            elif cnt==1:
                loc=[loc[0],loc[1]+1]
                res[loc[0]][loc[1]]=num
            elif cnt==2:
                loc=[loc[0]-1,loc[1]-1]
                res[loc[0]][loc[1]]=num
        cnt=(cnt+1)%3
        n-=1
    for child in res:
        for nchild in child:
            answer.append(nchild)
    return answer