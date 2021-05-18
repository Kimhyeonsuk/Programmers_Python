def intToStr(num):
    h=(str(num//60)).zfill(2)
    m=(str(num%60)).zfill(2)
    return h+":"+m

def solution(n, t, m, timetable):
    answer = 0
    timelist=[]
    for strs in timetable:
        sp=strs.split(':')
        h=int(sp[0])
        minute=int(sp[1])
        timelist.append(h*60+minute)
    timelist.sort()

    for i in range(n):
        busTime=540+t*i
        busmember=[]
        while timelist and timelist[0]<=busTime:
            busmember.append(timelist.pop(0))
            if len(busmember)==m:break

        if len(busmember)<m:
            answer=max(answer,busTime)
        elif busmember:
            tmp=busmember[-1]
            answer=max(answer,tmp-1)
    return intToStr(answer)