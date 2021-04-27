def strtotime(timeStr):
    timeSp=''.join(timeStr).split(':')
    return int(timeSp[0])*60+int(timeSp[1])
def timetostr(time):
    h=str(time//60)
    m=str(time%60)
    if len(h)==1:
        h='0'+h
    if len(m)==1:
        m='0'+m
    return h+':'+m
def solution(n, t, m, timetable):
    answer = ''
    allTime = [0] * 1440
    numberTimeTable=[]
    for time in timetable:
        allTime[strtotime(time)]+=1
    busTime = []
    for i in range(n):
        busTime.append(strtotime('09:00')+i*t)
    cnt = 0
    for i in range(1440):
        if allTime[i]!=0:
            cnt+=allTime[i]
            allTime[i]=cnt
        else:
            allTime[i]=cnt

        if busTime:
            if busTime[0]==i:
                if allTime[i]<m:
                    answer=busTime[0]
                    cnt=0
                elif allTime[i]>=m:
                    differ=abs(m-allTime[i])
                    for minute in range(i-1,-1,-1):
                        if allTime[i]-allTime[minute]>differ:
                            answer=minute
                            cnt=differ
                            break
                busTime.pop(0)
        else:
            break
    answer=timetostr(answer)
    return answer