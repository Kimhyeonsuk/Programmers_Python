def solution(S):
    res=0
    check=[0 for _ in range(26)]
    for i in S:
        if check[ord(i)-ord('a')]%2==0:
            res+=1
        else:
            res-=1
        check[ord(i)-ord('a')]+=1
    return res

def solutiontwo(N):
    check=[]
    for iIndex,i in enumerate(str(N)):
        if i=='5':
            tmp=str(N)[:iIndex]+str(N)[iIndex+1:]
            check.append(int(tmp))
    check=sorted(check,reverse=True)
    return check[0]