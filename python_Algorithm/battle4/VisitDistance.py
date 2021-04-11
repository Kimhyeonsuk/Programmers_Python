def solution(dirs):
    answer = 0
    map=dict()
    for x in range(-5,6):
        for y in range(-5,6):
            xyString=str(x)+str(y)
            map[xyString]=[False,False,False,False]
    x,y=(0,0)
    # 상 , 하 , 좌, 우
    for dir in dirs:
        xyString=str(x)+str(y)
        if dir=='R' and x+1!=6:
            nextString=str(x+1)+str(y)
            if map[xyString][0] == False and map[nextString][1] == False:
                map[xyString][0] = True
                map[nextString][1] = True
                answer += 1
            x = x + 1
        elif dir=='D' and y-1!=-6:
            nextString = str(x) + str(y-1)
            if map[xyString][2]==False and map[nextString][3]==False:
                map[xyString][2]=True
                map[nextString][3]=True
                answer+=1
            y=y-1
        elif dir=='U' and y+1!=6:
            nextString = str(x) + str(y+ 1)
            if map[xyString][3]==False and map[nextString][2]==False:
                map[xyString][3]=True
                map[nextString][2]=True
                answer+=1
            y=y+1
        elif dir=='L' and x-1!=-6:
            nextString = str(x-1) + str(y)
            if map[xyString][1]==False and map[nextString][0]==False:
                map[xyString][1]=True
                map[nextString][0]=True
                answer+=1
            x=x-1
    return answer