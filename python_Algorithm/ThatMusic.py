import re
def strToTime(timeStr):
    sp=timeStr.split(':')
    h=int(sp[0])*60
    m=int(sp[1])
    return h+m
def solution(m, musicinfos):
    answer = ''
    m = ''.join(m).replace('C#', 'X')
    m = ''.join(m).replace('D#', 'Y')
    m= ''.join(m).replace('F#', 'Z')
    m = ''.join(m).replace('G#', 'W')
    m = ''.join(m).replace('A#', 'P')

    maxlen=0
    for musicinfo in musicinfos:
        sp=musicinfo.split(',')
        playTime=strToTime(sp[1])-strToTime(sp[0])
        music=''.join(sp[3]).replace('C#','X')
        music = ''.join(music).replace('D#', 'Y')
        music = ''.join(music).replace('F#', 'Z')
        music = ''.join(music).replace('G#', 'W')
        music = ''.join(music).replace('A#', 'P')
        res=''
        for i in range(playTime):
            res+=music[i%len(music)]
        findIdx=res.find(m)
        if findIdx!=-1 and len(res)>maxlen:
            maxlen=len(res)
            answer=sp[2]
    if answer=='':
        answer='(None)'
    return answer