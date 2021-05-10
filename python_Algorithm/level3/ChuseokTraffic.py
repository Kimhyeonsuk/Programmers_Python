def strToInt(strs):
    sp=''.join(strs).split(':')
    h=int(sp[0])*60*60*1000
    m=int(sp[1])*60*1000
    s=int((sp[2].split('.'))[0])*1000
    return h+m+s+int((sp[2].split('.'))[1])
def solution(lines):
    answer = 0
    info=[]
    for line in lines:
        sp=''.join(line).split(' ')
        time=strToInt(sp[1])
        play=float(sp[2][:-1])*1000
        info.append((time-play+1,time))

    for idx,infoTime in enumerate(info):
        finTime=infoTime[1]
        nfinTime=infoTime[1]+999
        cnt=1
        for jdx in range(idx+1,len(info)):
            if info[jdx][0]<=nfinTime:
                cnt+=1
        answer=max(answer,cnt)
    return answer