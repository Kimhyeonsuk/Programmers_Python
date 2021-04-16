def permu(x,y,length,arr):
    n=int(length/2)
    oNum=0
    for i in range(x,x+length):
        for j in range(y,y+length):
            if arr[i][j]==1:
                oNum+=1
    if oNum==length*length:
        return (0,1)
    elif oNum==0:
        return (1,0)
    else:
        a=tuple([a+b for a,b in zip(permu(x,y,n,arr),permu(x+n,y+n,arr))])
        b=tuple([a+b for a,b in zip(permu(x+n,y,n,arr),permu(x,y+n,arr))])
        return tuple([x+y for x,y, in zip(a,b)])

def solution(arr):
    answer=[0,0]
    val=permu(0,0,len(arr),arr)
    answer[0]=val[0]
    answer[1]=val[1]
    return answer