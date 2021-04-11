import math
def solution(n, stations, w):
    answer = 0
    unit=w*2+1
    answer+=math.ceil((stations[0]-1-w)/unit)
    for idx in range(1,len(stations)):
        betweenNum=stations[idx]-stations[idx-1]-1-(2*w)
        if betweenNum>0:
            answer+=math.ceil(betweenNum/unit)

    leftNum=n-stations[-1]-w
    if leftNum>0:
        answer+=math.ceil(leftNum/unit)

    return answer