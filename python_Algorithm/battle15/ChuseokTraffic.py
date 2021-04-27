

def strToInt(timeStr):
    sp=''.join(timeStr).split(':')
    h=int(sp[0])*60*60*1000
    m=int(sp[1])*60*1000
    c=int(float(sp[2])*1000)
    return h+m+c
def solution(lines):
    answer = 0
    endlist=[]
    startList=[]
    pairlist=[]
    for line in lines:
        sp=''.join(line).split(' ')
        finTime=strToInt(sp[1])
        procTime=int(float(''.join(sp[2][:-1]))*1000)
        startTime=finTime-(procTime-1)
        pairlist.append((startTime,finTime))
    for pair1 in pairlist:
        unitStart=pair1[1]
        unitEnd=pair1[1]+999
        cnt=0
        for pair2 in pairlist:
            if pair2[0]<=unitEnd and pair2[1]>=pair1[1]:
                cnt+=1
        answer=max(answer,cnt)
    return answer