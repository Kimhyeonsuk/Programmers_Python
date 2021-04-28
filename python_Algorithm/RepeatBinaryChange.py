import re
def solution(s):
    answer = []
    zeroNum=0
    cnt=0
    while s!='1':
        tmps=re.sub('0','',s)
        strlen=len(tmps)
        zeroNum+=len(s)-len(tmps)
        nextstr=''
        while strlen!=0:
            if strlen%2==0:
                nextstr = nextstr + '0'
            else:
                nextstr=nextstr+'1'
            strlen=strlen//2
        s=nextstr
        cnt+=1
    return [cnt,zeroNum]