def solution(n,k,cmd):
    answer=[]
    tmp=[]
    li=[i for i in range(n)]
    for cmdInfo in cmd:
        if cmdInfo[0]=='U':
            k-=int((cmdInfo.split(' '))[1])
        elif cmdInfo[0]=='D':
            k+=int((cmdInfo.split(' '))[1])
        elif cmdInfo[0]=='C':
            tmp.append((li[k],k))
            li=li[:k]+li[k+1:]
            if k==len(li):
                k-=1
        elif cmdInfo[0]=='Z':
            val=tmp.pop()
            if val[1]<=k:
                k+=1
            li=li[:val[1]]+[val[0]]+li[val[1]:]
    li=set(li)
    for i in range(n):
        if i not in li:
            answer.append('X')
        else:
            answer.append('O')
    return ''.join(answer)