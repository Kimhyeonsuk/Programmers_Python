def permu(x,y,num,arr):
    ocnt=0
    for i in range(x,x+num):
        for j in range(y,y+num):
            if arr[i][j]==1:
                ocnt+=1
    if ocnt==num*num:
        return (0,1)
    elif ocnt==0:
        return (1,0)
    else:
        tupA=tuple(sum(ele) for ele in zip(permu(x,y,int(num/2),arr),permu(x+int(num/2),y,int(num/2),arr)))
        tupB=tuple(sum(ele) for ele in zip(permu(x+int(num/2),y+int(num/2),int(num/2),arr),permu(x,y+int(num/2),int(num/2),arr)))

        return tuple(sum(ele) for ele in zip(tupA,tupB))



def solution(arr):
    answer=[0,0]
    val=permu(0,0,len(arr),arr)
    answer[0]=val[0]
    answer[1]=val[1]
    return answer