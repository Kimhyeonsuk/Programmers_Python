def StrToTime(str):
    sp=''.join(str).split(':')
    h=int(sp[0])*60*60
    m=int(sp[1])*60
    s=int(sp[2])
    return h+m+s
def TimeToStr(time):
    s=time%60
    time=int(time/60)
    m=time%60
    h=int(time/60)

    res=''
    if(len(str(h))==1):res+='0'+str(h)
    else:res+=str(h)
    res+=':'
    if (len(str(m)) == 1):
        res += '0' + str(m)
    else:
        res += str(m)
    res+=':'
    if (len(str(s)) == 1):
        res += '0' + str(s)
    else:
        res += str(s)
    return res

def solution(play_time, adv_time, logs):
    answer = ''
    advTime=StrToTime(adv_time)
    playTime=StrToTime(play_time)
    allTime=[0]*360001
    for log in logs:
        sp=''.join(log).split('-')
        start=StrToTime(sp[0])
        end=StrToTime(sp[1])
        allTime[start]+=1
        allTime[end]-=1
    tmp=0
    for i in range(1,playTime+1):
        allTime[i]=allTime[i]+allTime[i-1];
    for i in range(1,playTime+1):
        allTime[i]=allTime[i]+allTime[i-1];

    mostView=allTime[advTime-1]
    mostViewtime=0
    for i in range(advTime,playTime):
        play=allTime[i]-allTime[i-advTime]

        if mostView<play:
            mostView=play
            mostViewtime=i-advTime+1


    return TimeToStr(mostViewtime)