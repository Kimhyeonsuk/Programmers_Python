import re
def solution(s):
    answer = []
    cnt=0
    zNum=0
    while s!='1':
        strList=list(s)
        zNum+=strList.count('0')
        s=re.sub('0','',s)
        numlen=len(s)

        res=''
        while numlen>0:
            res+=str(numlen%2)
            numlen=int(numlen/2)
        s=res
        cnt+=1
    answer.append(cnt)
    answer.append(zNum)
    return answer