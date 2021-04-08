def compression(unitSize,s):
    res=''
    tmp=''
    cnt=0
    for us in range(0,len(s),unitSize):
        if tmp!=s[us:us+unitSize]:
            if cnt==1:
                res+=tmp
            elif cnt>1:
                res+=str(cnt)+tmp
            cnt = 1
            tmp = s[us:us + unitSize]
        else:
            cnt+=1
    if cnt==1:
        res+=tmp
    elif cnt>1:
        res+=str(cnt)+tmp
    return res
def solution(s):
    answer = 1e9
    if len(s)==1:
        answer=1
    for unitSize in range(1, int(len(s)/2)+1):
        compressed=compression(unitSize,s)
        answer=min(answer,len(compressed))
    return answer